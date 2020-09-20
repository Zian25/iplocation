# -*- coding: utf-8 -*-
"""Inicio pinghavel"""
import re
import subprocess
import platform
import requests
from bs4 import BeautifulSoup as Beaut

sistema = platform.system()

ping_errors = ["Esgotado o tempo limite do pedido", "Destination host unreachable",
               "A solicitação ping não pôde encontrar o host", "Destination host unreachable",
               "Request timed out", "0 received", "Name or service not known"]


class Pinghavel:
    """Classe principal que retorna informações de ip"""

    def __init__(self):
        pass

    @staticmethod
    def getip():
        """Retorna o ip externo do usuario que solicitou"""
        try:
            url = "https://www.meuip.com.br/"
            getter = requests.get(url)
            if int(getter.status_code) == 200:
                scanner = Beaut(getter.text, 'html.parser')
                gettip = scanner.find('h3', class_='m-0 font-weight-bold')
                ip = gettip.text.replace("Meu ip é ", "")
                return ip

            return "Host indisponivel"

        except requests.exceptions.ConnectionError:
            return "Host indisponivel"

    def pingavel(self, ip=None):
        """Retorna se o ip é pingavel"""
        i = 0
        if ip is None:
            ip = self.getip()

        if sistema == "Windows":
            proc = subprocess.Popen(f"ping {ip} -n 1",
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            tmp = proc.stdout.read().decode('windows-1252')

            for i in range(len(ping_errors)):
                item = ping_errors[i]
                if re.search(item, tmp):
                    return False

            return True

        elif sistema == "Linux":
            proc = subprocess.Popen(f"ping -c 1 {ip}",
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT,
                                    shell=True)
            tmp = proc.stdout.read().decode('utf-8')
            for i in range(len(ping_errors)):
                item = ping_errors[i]
                if re.search(item, tmp):
                    return False

            return True
