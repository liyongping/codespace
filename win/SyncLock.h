// SyncLock.h: interface for the CSyncLock class.
//
//////////////////////////////////////////////////////////////////////

#if !defined(AFX_SYNCLOCK_H__BE91D373_1A2E_4FDC_989F_3445483CB8A8__INCLUDED_)
#define AFX_SYNCLOCK_H__BE91D373_1A2E_4FDC_989F_3445483CB8A8__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000
#define _WIN32_WINNT 0x500

#include <windows.h>

class CSyncLock  
{
public:
	CSyncLock(){
		//InitializeCriticalSection(&m_csLock);
		InitializeCriticalSectionAndSpinCount(&m_csLock,0);//4000 maybe good.
	}
	virtual ~CSyncLock(){
		DeleteCriticalSection(&m_csLock);
	}

	void Lock(){
		EnterCriticalSection(&m_csLock);
	}
	void Unlock(){
		LeaveCriticalSection(&m_csLock);
	}
private:
	CRITICAL_SECTION m_csLock;
};

#endif // !defined(AFX_SYNCLOCK_H__BE91D373_1A2E_4FDC_989F_3445483CB8A8__INCLUDED_)
