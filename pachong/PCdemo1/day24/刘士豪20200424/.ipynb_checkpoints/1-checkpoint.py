{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 读取数据，生成DataFrame对象"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          key  num\n",
      "0  2018-12-03    1\n",
      "1  2018-12-04    2\n",
      "2  2018-12-05    9\n",
      "3  2018-12-06    5\n",
      "4  2018-12-07    5\n"
     ]
    }
   ],
   "source": [
    "date1=np.loadtxt('./data/SGXCN.txt',dtype=str,skiprows=1)\n",
    "date1=pd.DataFrame({\n",
    "    'key':date1,\n",
    "    'num':np.random.randint(0,5,5)\n",
    "})\n",
    "print(date1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          key  num\n",
      "0  2018-12-01    0\n",
      "1  2018-12-02    8\n",
      "2  2018-12-03    4\n",
      "3  2018-12-04    3\n",
      "4  2018-12-05    1\n"
     ]
    }
   ],
   "source": [
    "date2=np.loadtxt('./data/HS300.txt',dtype=str,skiprows=1)\n",
    "date2=pd.DataFrame({\n",
    "    'key':date2,\n",
    "    'num':np.random.randint(0,5,5)\n",
    "})\n",
    "print(date2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 左右连接可以判断是否匹配，不能匹配说明不相同"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          key  num\n",
      "0  2018-12-03    1\n",
      "1  2018-12-04    2\n",
      "2  2018-12-05    9\n",
      "3  2018-12-06    5\n",
      "4  2018-12-07    5\n",
      "          key  num\n",
      "0  2018-12-01    0\n",
      "1  2018-12-02    8\n",
      "2  2018-12-03    4\n",
      "3  2018-12-04    3\n",
      "4  2018-12-05    1\n",
      "          key  num_x  num_y\n",
      "0  2018-12-03      1    4.0\n",
      "1  2018-12-04      2    3.0\n",
      "2  2018-12-05      9    1.0\n",
      "3  2018-12-06      5    NaN\n",
      "4  2018-12-07      5    NaN\n",
      "0    False\n",
      "1    False\n",
      "2    False\n",
      "3     True\n",
      "4     True\n",
      "Name: num_y, dtype: bool\n",
      "          key  num\n",
      "3  2018-12-06    5\n",
      "4  2018-12-07    5\n"
     ]
    }
   ],
   "source": [
    "print(date1)\n",
    "print(date2)\n",
    "date=pd.merge(date1,date2,on='key',how='left')\n",
    "print(date)\n",
    "is_null=date['num_y'].isnull()\n",
    "print(is_null)\n",
    "date=date1[is_null]\n",
    "print(date)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          key  num\n",
      "0  2018-12-03    1\n",
      "1  2018-12-04    2\n",
      "2  2018-12-05    9\n",
      "3  2018-12-06    5\n",
      "4  2018-12-07    5\n",
      "          key  num\n",
      "0  2018-12-01    0\n",
      "1  2018-12-02    8\n",
      "2  2018-12-03    4\n",
      "3  2018-12-04    3\n",
      "4  2018-12-05    1\n",
      "          key  num_x  num_y\n",
      "0  2018-12-01      0    NaN\n",
      "1  2018-12-02      8    NaN\n",
      "2  2018-12-03      4    1.0\n",
      "3  2018-12-04      3    2.0\n",
      "4  2018-12-05      1    9.0\n",
      "0     True\n",
      "1     True\n",
      "2    False\n",
      "3    False\n",
      "4    False\n",
      "Name: num_y, dtype: bool\n",
      "          key  num\n",
      "0  2018-12-01    0\n",
      "1  2018-12-02    8\n"
     ]
    }
   ],
   "source": [
    "# HS300.txt中出现，SGX CN.txt没出现的日期\n",
    "\n",
    "print(date1)\n",
    "print(date2)\n",
    "date=pd.merge(date2,date1,on='key',how='left')\n",
    "\n",
    "print(date)\n",
    "is_null=date['num_y'].isnull()\n",
    "print(is_null)\n",
    "date=date2[is_null]\n",
    "print(date)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
