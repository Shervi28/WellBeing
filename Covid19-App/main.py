from time import sleep
from os import system, name 
from rich.console import Console
from pyfiglet import Figlet, figlet_format
from topic1 import main
from topic2 import main2
from topic3 import main3
from covid import covid
from chatbot import docbot
from topic6 import main6

console = Console()

print(figlet_format("Well-Being", font = "5lineoblique" ))

def clear(): 
  
  if name == 'nt': 
       
    _ = system('cls') 
    
  else: 
       
    _ = system('clear') 

console.print("[red]Hi I am your well being health bot, I can assist you and make you a better person, phsyically, mentally and healthily.[/red]")
console.print("\n")
sleep(2)
console.print("[red]What should I help you with?[/red]")
console.print("\n")
sleep(3)
console.print("[yellow]1.Diseases[/yellow]")
console.print("\n")
console.print("[green]2.Mental Health[/green]")
console.print("\n")
console.print("[magenta]3.Physical Pain[/magenta]")
console.print("\n")
console.print("[orange]4.Covid19[/orange]")
console.print("\n")
console.print("[red]5.Chat with docbot")
console.print("\n")
console.print("[yellow]6.Pills[/yellow]")
console.print("\n")
#console.print("[brown]7.Dashboard[/brown]")
topics=input("---->Please Enter a number: ")
print("\n")

if topics == "1":
  main()

if topics == "2":
  main2()

if topics == "3":
  main3()

if topics == "4":
  covid()

if topics == "5":
  docbot()
  
if topics == "6":
  main6()
else:
  clear()