/**
 * @file   daemon.c
 * @author vincent lee(lypkiller@gmail.com)
 * @date   Sun Apr 15 23:09:37 2012
 * 
 * @brief  参考自memcached，方便创建守护进程
 * 
 * 
 */

#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/** 
 * 调用本函数，将使当前进程成为守护进程
 * 
 * @param nochdir 设置是否更改原进程的默认工作目录，0表示将修改默认的当前工作目录到“/”,其它值表示不做更改
 * @param noclose 设置是否关闭原进程的stdin,stdout,stderr三个流,0表示关闭，其它值表示不关闭，建议为0
 * 
 * @return 0表示成功，-1表示失败
 */
int daemonize(int nochdir, int noclose)
{
    int fd;

    switch (fork()) {
    case -1:    // 出错
        return (-1);
    case 0:     // 子进程
        break;
    default:    // 父进程，退出
        _exit(EXIT_SUCCESS);
    }
    // setsid函数将创建新的会话，并使得调用setsid函数的进程成为新会话的领头进程
    if (setsid() == -1)
        return (-1);

    if (nochdir == 0) {
        // 使用fork函数产生的子进程将继承父进程的当前工作目录。当进程没有结束时，其工作目录是不能被卸载的。
        // 为了防止这种问题发生，守护进程一般会将其工作目录更改到根目录下（/目录）
        if(chdir("/") != 0) {
            perror("chdir");
            return (-1);
        }
    }

    if (noclose == 0 && (fd = open("/dev/null", O_RDWR, 0)) != -1) {
        // 新产生的进程从父进程继承了某些打开的文件描述符，如果不使用这些文件描述符，则需要关闭它们
        if(dup2(fd, STDIN_FILENO) < 0) {    // 把stdin重定向到/dev/null
            perror("dup2 stdin");
            return (-1);
        }
        if(dup2(fd, STDOUT_FILENO) < 0) {
            perror("dup2 stdout");
            return (-1);
        }
        if(dup2(fd, STDERR_FILENO) < 0) {
            perror("dup2 stderr");
            return (-1);
        }

        if (fd > STDERR_FILENO) {
            if(close(fd) < 0) {
                perror("close");
                return (-1);
            }
        }
    }
    return (0);
}

#ifdef UNIT_TEST
/**
 * if you try to run this unit test,please do:
 * complie: gcc daemon.c -o daemon.out -DUNIT_TEST
 */

int main(int argc, char *argv[])
{
    printf ("hi,i will run as daemon process\n");
    if(0 != daemonize(0,0))
        printf ("run as daemon process unsuccessfully\n");
    sleep(5);
    return 0;
}
#endif
