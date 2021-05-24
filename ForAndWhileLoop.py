{
  "nbformat": 4,
  "nbformat_minor": 0,
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
      "version": "3.7.6"
    },
    "colab": {
      "name": "ForAndWhileLoop.ipynb",
      "provenance": [],
      "include_colab_link": true
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ArcotSiri/Python/blob/main/ForAndWhileLoop.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "x-Cu51T4tYdI"
      },
      "source": [
        "## Loops"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "1Ql2LHRatYdU"
      },
      "source": [
        "#### For Loop"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "0mKLyhlXtYdW"
      },
      "source": [
        "colours = [\"Violet\",\"Indigo\",\"Blue\",\"Green\",\"Yellow\",\"Orange\",\"Red\"]"
      ],
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8ivU7bDCtYdY",
        "outputId": "e24b4111-65d1-46b7-d629-65f6c8649725"
      },
      "source": [
        "for colour in colours:\n",
        "    print(colour)"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Violet\n",
            "Indigo\n",
            "Blue\n",
            "Green\n",
            "Yellow\n",
            "Orange\n",
            "Red\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "sC0iGYKytYdZ"
      },
      "source": [
        "#### For Loop with range"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "f18ljD4EtYda",
        "outputId": "942accda-d10d-41c7-fdec-5dd15d353183"
      },
      "source": [
        "for i in range(0,10):\n",
        "    print(i)"
      ],
      "execution_count": 3,
      "outputs": [
        {
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
            "9\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "qrNdOACytYdb"
      },
      "source": [
        "#### While Loop"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UmO1k3NmtYdb",
        "outputId": "51ab4aff-60a7-4ee5-efb6-fc47e59ea351"
      },
      "source": [
        "i = 10\n",
        "while(i>0):\n",
        "    print(i)\n",
        "    i-=1"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "10\n",
            "9\n",
            "8\n",
            "7\n",
            "6\n",
            "5\n",
            "4\n",
            "3\n",
            "2\n",
            "1\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "gFBpa6tOtYdc"
      },
      "source": [
        "#### Run the loop as long as the user wants to using `break`"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ujRMSnhctYdd",
        "outputId": "60e10249-71f0-4a80-f600-a4b9e0fe201b"
      },
      "source": [
        "while(True): #Infinite loop\n",
        "    print(\"Hello\")\n",
        "    shouldWeContinue = input(\"Do you want to continue Y/N? \")\n",
        "    if(shouldWeContinue == \"N\"):\n",
        "        break\n",
        "        "
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Hello\n",
            "Do you want to continue Y/N? y\n",
            "Hello\n",
            "Do you want to continue Y/N? y\n",
            "Hello\n",
            "Do you want to continue Y/N? n\n",
            "Hello\n",
            "Do you want to continue Y/N? ggyu\n",
            "Hello\n",
            "Do you want to continue Y/N? N\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "k2kfvu-EtYde"
      },
      "source": [
        "#### Print all numbers between 1 to 100 except the ones which are divisible by 9 "
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "g79Ps7CqtYde",
        "outputId": "75829689-7ab2-43f8-ff54-70f01483d25e"
      },
      "source": [
        "for i in range(1,101):\n",
        "    if(i%9 == 0):\n",
        "        continue\n",
        "        \n",
        "    print(i)\n",
        "    "
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "5\n",
            "6\n",
            "7\n",
            "8\n",
            "10\n",
            "11\n",
            "12\n",
            "13\n",
            "14\n",
            "15\n",
            "16\n",
            "17\n",
            "19\n",
            "20\n",
            "21\n",
            "22\n",
            "23\n",
            "24\n",
            "25\n",
            "26\n",
            "28\n",
            "29\n",
            "30\n",
            "31\n",
            "32\n",
            "33\n",
            "34\n",
            "35\n",
            "37\n",
            "38\n",
            "39\n",
            "40\n",
            "41\n",
            "42\n",
            "43\n",
            "44\n",
            "46\n",
            "47\n",
            "48\n",
            "49\n",
            "50\n",
            "51\n",
            "52\n",
            "53\n",
            "55\n",
            "56\n",
            "57\n",
            "58\n",
            "59\n",
            "60\n",
            "61\n",
            "62\n",
            "64\n",
            "65\n",
            "66\n",
            "67\n",
            "68\n",
            "69\n",
            "70\n",
            "71\n",
            "73\n",
            "74\n",
            "75\n",
            "76\n",
            "77\n",
            "78\n",
            "79\n",
            "80\n",
            "82\n",
            "83\n",
            "84\n",
            "85\n",
            "86\n",
            "87\n",
            "88\n",
            "89\n",
            "91\n",
            "92\n",
            "93\n",
            "94\n",
            "95\n",
            "96\n",
            "97\n",
            "98\n",
            "100\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "HN5ghWChtYdf"
      },
      "source": [
        "#### Challenge\n",
        "Take two number inputs from the user and ask the user to choose the operation to perform ie., +,-,*,/,\\**. Depending on what the user input is, perform operation and print output.If the user input is not one of the operations mentioned, print appropriate message. "
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1KPJzU42tYdg",
        "outputId": "9f213df5-b7b9-4c31-ba23-bead2a11e37d"
      },
      "source": [
        "print('Enter the first number : ')\n",
        "a = int(input())\n",
        "print('Enter the second number : ')\n",
        "b = int(input())\n",
        "print('Choose the operation to perform + or - or / or *')\n",
        "op = input()\n",
        "\n",
        "if op=='+':\n",
        "  ans = a+b\n",
        "  print(ans)\n",
        "elif op=='-':\n",
        "  ans = a-b\n",
        "  print(ans)\n",
        "elif op=='/':\n",
        "  ans = a/b\n",
        "  print(ans)\n",
        "elif op=='*':\n",
        "  ans = a*b\n",
        "  print(ans)\n",
        "else:\n",
        "  print('Please enter only arithmetic operation to be performed')\n"
      ],
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Enter the first number : \n",
            "2\n",
            "Enter the second number : \n",
            "9\n",
            "Choose the operation to perform + or - or / or *\n",
            "*\n",
            "18\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "cyiUzSYWtYdg"
      },
      "source": [
        "Double-click __here__ for the solution.\n",
        "\n",
        "<!--\n",
        "num1 = int(input(\"Enter the first number \"))\n",
        "num2 = int(input(\"Enter the second number\"))\n",
        "\n",
        "op = input(\"What operation do you want perform? \")\n",
        "\n",
        "if(op == \"+\"):\n",
        "    print(num1+num2)\n",
        "elif (op == \"-\"):\n",
        "    print(num1-num2)\n",
        "elif (op == \"*\"):\n",
        "    print(num1*num2)\n",
        "elif (op == \"/\"):\n",
        "    print(num1/num2)\n",
        "elif (op == \"**\"):\n",
        "    print(num1**num2)\n",
        "else:\n",
        "    print(\"Not a valid operation\")\n",
        "-->"
      ]
    }
  ]
}