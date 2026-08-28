{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMfvie+6GSPPHOQ9L4pewDg",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
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
        "<a href=\"https://colab.research.google.com/github/shagunSrivastava9797-oss/CODSOFT_TASKSNO/blob/main/Password%20generator.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FWI2QTd2wzQS",
        "outputId": "7ff1853c-12fd-43d5-f9ca-dcea883cffff"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "===== PASSWORD GENERATOR =====\n",
            "\n",
            "Enter desired password length: 12\n",
            "Include letters? (y/n): Y\n",
            "Include digits? (y/n): Y\n",
            "Include symbols? (y/n): Y\n",
            "\n",
            "Generated Password: &@`/=!>$Z$n-\n",
            "\n",
            "Generate another password? (y/n): Y\n",
            "\n",
            "Enter desired password length: 10\n",
            "Include letters? (y/n): Y\n",
            "Include digits? (y/n): Y\n",
            "Include symbols? (y/n): Y\n",
            "\n",
            "Generated Password: )$z-m)'E3v\n",
            "\n",
            "Generate another password? (y/n): N\n",
            "Goodbye!\n"
          ]
        }
      ],
      "source": [
        "import random\n",
        "import string\n",
        "\n",
        "\n",
        "def generate_password(length, use_letters=True, use_digits=True, use_symbols=True):\n",
        "    characters = \"\"\n",
        "    if use_letters:\n",
        "        characters += string.ascii_letters\n",
        "    if use_digits:\n",
        "        characters += string.digits\n",
        "    if use_symbols:\n",
        "        characters += string.punctuation\n",
        "\n",
        "    if not characters:\n",
        "        return None\n",
        "\n",
        "    password = \"\".join(random.choice(characters) for _ in range(length))\n",
        "    return password\n",
        "\n",
        "\n",
        "def get_yes_no(prompt):\n",
        "    while True:\n",
        "        answer = input(prompt).strip().lower()\n",
        "        if answer in (\"y\", \"yes\"):\n",
        "            return True\n",
        "        elif answer in (\"n\", \"no\"):\n",
        "            return False\n",
        "        else:\n",
        "            print(\"Please enter y or n.\")\n",
        "\n",
        "\n",
        "def main():\n",
        "    print(\"===== PASSWORD GENERATOR =====\")\n",
        "\n",
        "    while True:\n",
        "        try:\n",
        "            length = int(input(\"\\nEnter desired password length: \"))\n",
        "            if length <= 0:\n",
        "                print(\"Length must be a positive number.\")\n",
        "                continue\n",
        "        except ValueError:\n",
        "            print(\"Please enter a valid number.\")\n",
        "            continue\n",
        "\n",
        "        include_letters = get_yes_no(\"Include letters? (y/n): \")\n",
        "        include_digits = get_yes_no(\"Include digits? (y/n): \")\n",
        "        include_symbols = get_yes_no(\"Include symbols? (y/n): \")\n",
        "\n",
        "        password = generate_password(length, include_letters, include_digits, include_symbols)\n",
        "\n",
        "        if password is None:\n",
        "            print(\"You must select at least one character type.\")\n",
        "        else:\n",
        "            print(f\"\\nGenerated Password: {password}\")\n",
        "\n",
        "        again = input(\"\\nGenerate another password? (y/n): \").strip().lower()\n",
        "        if again not in (\"y\", \"yes\"):\n",
        "            print(\"Goodbye!\")\n",
        "            break\n",
        "\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    main()"
      ]
    }
  ]
}