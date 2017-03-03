#ifndef _QUERYPERFORMANCE_H_
#define _QUERYPERFORMANCE_H_
#include <Windows.h>

class CQueryPerformance
{
public:

	CQueryPerformance(void){
		QueryPerformanceFrequency(&m_liPerfFreq);
	}

	~CQueryPerformance(void){}

	void Start(){
		QueryPerformanceCounter(&m_liPerfStart);
	}
	
	__int64 Stop(){
		LARGE_INTEGER liPerfNow;
		QueryPerformanceCounter(&liPerfNow);
		return (((liPerfNow.QuadPart-m_liPerfStart.QuadPart)*1000)/m_liPerfFreq.QuadPart);
	}
	
private:
	LARGE_INTEGER m_liPerfFreq;
	LARGE_INTEGER m_liPerfStart;
};

#endif



