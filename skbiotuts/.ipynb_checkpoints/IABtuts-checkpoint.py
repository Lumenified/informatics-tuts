{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Populating the interactive namespace from numpy and matplotlib\n"
     ]
    }
   ],
   "source": [
    "%pylab inline\n",
    "import numpy as np\n",
    "from IPython.core.display import HTML\n",
    "from IPython.core import page\n",
    "page.page = print"
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
      "ACCCAGGTTAACGGTGACCAGGTACCAGAAGGGTACCAGGTAGGACACACGGGGATTAA\n",
      "ACCGAGGTTAACGGTGACCAGGTACCAGAAGGGTACCAGGTAGGAGACACGGCGATTAA\n",
      "TTCCAGGTAAACGGTGACCAGGTACCAGTTGCGTTTGTTGTAGGAGACACGGGGACCCA\n"
     ]
    }
   ],
   "source": [
    "from scipy.spatial.distance import hamming\n",
    "from skbio import DNA\n",
    "\n",
    "r1 = DNA(\"ACCCAGGTTAACGGTGACCAGGTACCAGAAGGGTACCAGGTAGGACACACGGGGATTAA\")\n",
    "r2 = DNA(\"ACCGAGGTTAACGGTGACCAGGTACCAGAAGGGTACCAGGTAGGAGACACGGCGATTAA\")\n",
    "q1 = DNA(\"TTCCAGGTAAACGGTGACCAGGTACCAGTTGCGTTTGTTGTAGGAGACACGGGGACCCA\")\n",
    "\n",
    "print(r1)\n",
    "print(r2)\n",
    "print(q1)"
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
      "\u001b[0;32mdef\u001b[0m \u001b[0mhamming\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mu\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mv\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mw\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\n",
      "\u001b[0;34m\u001b[0m    \u001b[0;34m\"\"\"\u001b[0m\n",
      "\u001b[0;34m    Compute the Hamming distance between two 1-D arrays.\u001b[0m\n",
      "\u001b[0;34m\u001b[0m\n",
      "\u001b[0;34m    The Hamming distance between 1-D arrays `u` and `v`, is simply the\u001b[0m\n",
      "\u001b[0;34m    proportion of disagreeing components in `u` and `v`. If `u` and `v` are\u001b[0m\n",
      "\u001b[0;34m    boolean vectors, the Hamming distance is\u001b[0m\n",
      "\u001b[0;34m\u001b[0m\n",
      "\u001b[0;34m    .. math::\u001b[0m\n",
      "\u001b[0;34m\u001b[0m\n",
      "\u001b[0;34m       \\\\frac{c_{01} + c_{10}}{n}\u001b[0m\n",
      "\u001b[0;34m\u001b[0m\n",
      "\u001b[0;34m    where :math:`c_{ij}` is the number of occurrences of\u001b[0m\n",
      "\u001b[0;34m    :math:`\\\\mathtt{u[k]} = i` and :math:`\\\\mathtt{v[k]} = j` for\u001b[0m\n",
      "\u001b[0;34m    :math:`k < n`.\u001b[0m\n",
      "\u001b[0;34m\u001b[0m\n",
      "\u001b[0;34m    Parameters\u001b[0m\n",
      "\u001b[0;34m    ----------\u001b[0m\n",
      "\u001b[0;34m    u : (N,) array_like\u001b[0m\n",
      "\u001b[0;34m        Input array.\u001b[0m\n",
      "\u001b[0;34m    v : (N,) array_like\u001b[0m\n",
      "\u001b[0;34m        Input array.\u001b[0m\n",
      "\u001b[0;34m    w : (N,) array_like, optional\u001b[0m\n",
      "\u001b[0;34m        The weights for each value in `u` and `v`. Default is None,\u001b[0m\n",
      "\u001b[0;34m        which gives each value a weight of 1.0\u001b[0m\n",
      "\u001b[0;34m\u001b[0m\n",
      "\u001b[0;34m    Returns\u001b[0m\n",
      "\u001b[0;34m    -------\u001b[0m\n",
      "\u001b[0;34m    hamming : double\u001b[0m\n",
      "\u001b[0;34m        The Hamming distance between vectors `u` and `v`.\u001b[0m\n",
      "\u001b[0;34m\u001b[0m\n",
      "\u001b[0;34m    Examples\u001b[0m\n",
      "\u001b[0;34m    --------\u001b[0m\n",
      "\u001b[0;34m    >>> from scipy.spatial import distance\u001b[0m\n",
      "\u001b[0;34m    >>> distance.hamming([1, 0, 0], [0, 1, 0])\u001b[0m\n",
      "\u001b[0;34m    0.66666666666666663\u001b[0m\n",
      "\u001b[0;34m    >>> distance.hamming([1, 0, 0], [1, 1, 0])\u001b[0m\n",
      "\u001b[0;34m    0.33333333333333331\u001b[0m\n",
      "\u001b[0;34m    >>> distance.hamming([1, 0, 0], [2, 0, 0])\u001b[0m\n",
      "\u001b[0;34m    0.33333333333333331\u001b[0m\n",
      "\u001b[0;34m    >>> distance.hamming([1, 0, 0], [3, 0, 0])\u001b[0m\n",
      "\u001b[0;34m    0.33333333333333331\u001b[0m\n",
      "\u001b[0;34m\u001b[0m\n",
      "\u001b[0;34m    \"\"\"\u001b[0m\u001b[0;34m\u001b[0m\n",
      "\u001b[0;34m\u001b[0m    \u001b[0mu\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_validate_vector\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mu\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\n",
      "\u001b[0;34m\u001b[0m    \u001b[0mv\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_validate_vector\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mv\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\n",
      "\u001b[0;34m\u001b[0m    \u001b[0;32mif\u001b[0m \u001b[0mu\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mshape\u001b[0m \u001b[0;34m!=\u001b[0m \u001b[0mv\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mshape\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\n",
      "\u001b[0;34m\u001b[0m        \u001b[0;32mraise\u001b[0m \u001b[0mValueError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'The 1d arrays must have equal lengths.'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\n",
      "\u001b[0;34m\u001b[0m    \u001b[0mu_ne_v\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mu\u001b[0m \u001b[0;34m!=\u001b[0m \u001b[0mv\u001b[0m\u001b[0;34m\u001b[0m\n",
      "\u001b[0;34m\u001b[0m    \u001b[0;32mif\u001b[0m \u001b[0mw\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\n",
      "\u001b[0;34m\u001b[0m        \u001b[0mw\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_validate_weights\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mw\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\n",
      "\u001b[0;34m\u001b[0m    \u001b[0;32mreturn\u001b[0m \u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0maverage\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mu_ne_v\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mweights\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mw\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\n"
     ]
    }
   ],
   "source": [
    "%psource hamming"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.2542372881355932\n",
      "0.2711864406779661\n"
     ]
    }
   ],
   "source": [
    "print(hamming(r1, q1))\n",
    "print(hamming(r2, q1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "TTCCAGGTAAACGGTGACCAGGTACCAGTTGCGTTTGTTGTAGGAGACACGGGGACCCA\n",
      "TCCAGGTAAACGGTGACCAGGTACCAGTTGCGTTTGTTGTAGGAGACACGGGGACCCAT\n",
      "0.7288135593220338\n"
     ]
    }
   ],
   "source": [
    "q2 = DNA(\"TCCAGGTAAACGGTGACCAGGTACCAGTTGCGTTTGTTGTAGGAGACACGGGGACCCAT\")\n",
    "\n",
    "print(q1)\n",
    "print(q2)\n",
    "\n",
    "print(hamming(r1, q2))"
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
 "nbformat_minor": 2
}
