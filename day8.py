{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "12e59787",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[5, 7, 10, 15, 23]\n"
     ]
    }
   ],
   "source": [
    "l=[5,7,23,10,15]\n",
    "for j in range (0,len(l)):\n",
    "    for i in range (0,len(l)-1-j):\n",
    "        if l[j]>l[j+1]:\n",
    "            l[j],l[j+1]=l[j+1],l[j]\n",
    "            \n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "93c8ab95",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "l=[2,6,9,1]\n",
    "for i in range (0,len(l)):\n",
    "    for j in range (0,len(l)-1-i):\n",
    "        if l[i]>l[i+1]:\n",
    "            min=l[i+1]\n",
    "print(min)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3161d2de",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 3, 5, 7, 8, 9, 10, 26, 44]\n"
     ]
    }
   ],
   "source": [
    "l=[9,7,5,8,10,26,44,3,1]\n",
    "for j in range (0,len(l)):\n",
    "    pos=j\n",
    "    min=l[j]\n",
    "    for i in range (j,len(l)):\n",
    "        if l[i]<min:\n",
    "            min=l[i]\n",
    "            pos=i\n",
    "    l[j],l[pos]= l[pos],l[j]\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "c2aef837",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "def print_num(n):\n",
    "    if n<=10:\n",
    "        print(n)\n",
    "        print_num(n+1)\n",
    "print_num(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "b9568330",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "8\n",
      "13\n"
     ]
    }
   ],
   "source": [
    "def fib(n):\n",
    "    if n==1:\n",
    "        return 0\n",
    "    if n==2:\n",
    "        return 1\n",
    "    return fib(n-1)+fib(n-2)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    n=int(input())\n",
    "    print(fib(n))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8b8e5546",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "120\n"
     ]
    }
   ],
   "source": [
    "#factorial\n",
    "def fact(n):\n",
    "    if n==0 or n==1:\n",
    "        return 1\n",
    "    else:\n",
    "        return n*fact(n-1)\n",
    "    \n",
    "if __name__ == \"__main__\":\n",
    "    n=int(input())\n",
    "    print(fact(n))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "f4670a8a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "99 88 77 66 55 44 33 22 11 00 1 2 3 4 5 6 7 8 9\n",
      "sorted array =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99]\n"
     ]
    }
   ],
   "source": [
    "#quick sort\n",
    "def divide(l,low,High):\n",
    "    p=l[High]\n",
    "    pi=High\n",
    "    j=low-1\n",
    "    for i in range (low,High):\n",
    "        if l[i]<=p:\n",
    "            j+=1\n",
    "            l[i],l[j]=l[j],l[i]\n",
    "    j+=1\n",
    "    l[j],l[pi]=l[pi],l[j]\n",
    "    pi=j\n",
    "    return pi\n",
    "\n",
    "def Quick_sort(l,low,High):\n",
    "    if low<High:\n",
    "        pi=divide(l,low,High)\n",
    "        Quick_sort(l,low,pi-1)\n",
    "        Quick_sort(l,pi+1,High)\n",
    "    return\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    l=list(map(int,input().split()))\n",
    "    Quick_sort(l,0,len(l)-1)\n",
    "    print(\"sorted array = \",l)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "31978878",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6 3 1 4 \n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "cannot unpack non-iterable int object",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Input \u001b[1;32mIn [15]\u001b[0m, in \u001b[0;36m<cell line: 23>\u001b[1;34m()\u001b[0m\n\u001b[0;32m     23\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;18m__name__\u001b[39m \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m__main__\u001b[39m\u001b[38;5;124m\"\u001b[39m:\n\u001b[0;32m     24\u001b[0m     l\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mlist\u001b[39m(\u001b[38;5;28mmap\u001b[39m(\u001b[38;5;28mint\u001b[39m,\u001b[38;5;28minput\u001b[39m()\u001b[38;5;241m.\u001b[39msplit()))\n\u001b[1;32m---> 25\u001b[0m     \u001b[43mMerge_sort\u001b[49m\u001b[43m(\u001b[49m\u001b[43ml\u001b[49m\u001b[43m,\u001b[49m\u001b[38;5;241;43m0\u001b[39;49m\u001b[43m,\u001b[49m\u001b[38;5;28;43mlen\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43ml\u001b[49m\u001b[43m)\u001b[49m\u001b[38;5;241;43m/\u001b[39;49m\u001b[38;5;241;43m/\u001b[39;49m\u001b[38;5;241;43m2\u001b[39;49m\u001b[43m,\u001b[49m\u001b[38;5;28;43mlen\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43ml\u001b[49m\u001b[43m)\u001b[49m\u001b[38;5;241;43m-\u001b[39;49m\u001b[38;5;241;43m1\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[0;32m     26\u001b[0m     Merge(l,\u001b[38;5;241m0\u001b[39m,\u001b[38;5;28mlen\u001b[39m(l)\u001b[38;5;241m-\u001b[39m\u001b[38;5;241m1\u001b[39m)\n\u001b[0;32m     27\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msorted array = \u001b[39m\u001b[38;5;124m\"\u001b[39m,l)\n",
      "Input \u001b[1;32mIn [15]\u001b[0m, in \u001b[0;36mMerge_sort\u001b[1;34m(l, low, mid, high)\u001b[0m\n\u001b[0;32m      3\u001b[0m right\u001b[38;5;241m=\u001b[39ml[mid\u001b[38;5;241m+\u001b[39m\u001b[38;5;241m1\u001b[39m:high]\n\u001b[0;32m      4\u001b[0m temp\u001b[38;5;241m=\u001b[39m[\u001b[38;5;241m0\u001b[39m]\u001b[38;5;241m*\u001b[39m\u001b[38;5;28mlen\u001b[39m(l)\n\u001b[1;32m----> 5\u001b[0m i,j,t\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m0\u001b[39m\n\u001b[0;32m      7\u001b[0m \u001b[38;5;28;01mwhile\u001b[39;00m i\u001b[38;5;241m<\u001b[39m\u001b[38;5;28mlen\u001b[39m(left) \u001b[38;5;129;01mand\u001b[39;00m j\u001b[38;5;241m<\u001b[39m\u001b[38;5;28mlen\u001b[39m(right):\n\u001b[0;32m      8\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m left[i]\u001b[38;5;241m<\u001b[39mright[j]:\n",
      "\u001b[1;31mTypeError\u001b[0m: cannot unpack non-iterable int object"
     ]
    }
   ],
   "source": [
    "def Merge_sort(l,low,mid,high):\n",
    "    left=l[low:mid]\n",
    "    right=l[mid+1:high]\n",
    "    temp=[0]*len(l)\n",
    "    i,j,t=0\n",
    "    \n",
    "    while i<len(left) and j<len(right):\n",
    "        if left[i]<right[j]:\n",
    "            temp[t]=right[j]\n",
    "            j+=1\n",
    "            t+=1\n",
    "    while i<len(left):\n",
    "        temp[t]=right[j]\n",
    "        j+=1\n",
    "        t+=1\n",
    "        \n",
    "def Merge(l,low,high):\n",
    "    if low<high:\n",
    "        mid=low+(high-low)//2\n",
    "        Merge(l,low,mid)\n",
    "        Merge_sort(l,low,mid,high)\n",
    "            \n",
    "if __name__ == \"__main__\":\n",
    "    l=list(map(int,input().split()))\n",
    "    Merge_sort(l,0,len(l)//2,len(l)-1)\n",
    "    Merge(l,0,len(l)-1)\n",
    "    print(\"sorted array = \",l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2926eba9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
