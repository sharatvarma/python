{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf470
{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 Menlo-Bold;\f2\fnil\fcharset0 Menlo-Regular;
}
{\colortbl;\red255\green255\blue255;\red32\green32\blue32;\red191\green100\blue38;\red153\green168\blue186;
\red14\green110\blue109;\red117\green114\blue185;\red86\green132\blue173;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx560\tx1120\tx1680\tx2240\tx2800\tx3360\tx3920\tx4480\tx5040\tx5600\tx6160\tx6720\pardirnatural\partightenfactor0

\f0\fs24 \cf0 \cb2 \uc0\u8232 
\f1\b \cf3 def \cf4 binarySearch
\f2\b0 ():\uc0\u8232     names = [\cf5 "Sharat"\cf3 , \cf5 "varma"\cf3 , \cf5 "chandra"\cf3 , \cf5 "pakalapati"\cf3 , \cf5 "murthy"\cf3 , \cf5 "Venky"\cf3 ,\uc0\u8232              \cf5 "dan"\cf3 , \cf5 "visu"\cf3 , \cf5 "ram"\cf3 , \cf5 "harish"\cf4 ]\uc0\u8232     names.sort()\u8232     name = \cf6 input\cf4 (\cf5 'What name are you looking for : '\cf4 )\uc0\u8232     lower_bound = \cf7 0\uc0\u8232     \cf4 upper_bound = \cf6 len\cf4 (names) - \cf7 1\uc0\u8232     \cf4 found = 
\f1\b \cf3 False\uc0\u8232     while 
\f2\b0 \cf4 lower_bound <= upper_bound 
\f1\b \cf3 and not 
\f2\b0 \cf4 found:\uc0\u8232         middle_pos = (lower_bound+upper_bound) // \cf7 2\uc0\u8232         
\f1\b \cf3 if 
\f2\b0 \cf4 names[middle_pos] < name:\uc0\u8232             lower_bound = middle_pos + \cf7 1\uc0\u8232         
\f1\b \cf3 elif 
\f2\b0 \cf4 names[middle_pos] > name:\uc0\u8232             upper_bound = middle_pos - \cf7 1\uc0\u8232         
\f1\b \cf3 else
\f2\b0 \cf4 :\uc0\u8232             found = 
\f1\b \cf3 True\uc0\u8232 \u8232     if 
\f2\b0 \cf4 found:\uc0\u8232         \cf6 print\cf4 (\cf5 "The name is at position"\cf3 , \cf4 middle_pos)\uc0\u8232     
\f1\b \cf3 else
\f2\b0 \cf4 :\uc0\u8232         \cf6 print\cf4 (\cf5 "The name was not in the list."\cf4 )\uc0\u8232 \u8232 \cf6 print\cf4 (binarySearch())\
}