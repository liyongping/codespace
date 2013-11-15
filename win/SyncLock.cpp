// SyncLock.cpp: implementation of the CSyncLock class.
//
//////////////////////////////////////////////////////////////////////

#include "SyncLock.h"

//////////////////////////////////////////////////////////////////////
// Construction/Destruction
//////////////////////////////////////////////////////////////////////

CSyncLock::CSyncLock()
{
	InitializeCriticalSectionAndSpinCount(&m_csLock,0);
}

CSyncLock::~CSyncLock()
{
	DeleteCriticalSection(&m_csLock);
}
void CSyncLock::Lock()
{
	EnterCriticalSection(&m_csLock);
}
void CSyncLock::Unlock()
{
	LeaveCriticalSection(&m_csLock);
}

