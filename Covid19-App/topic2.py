from time import sleep
from os import system, name 
from rich.console import Console
from pyfiglet import Figlet, figlet_format



console = Console()

def clear3(): 
  
  if name == 'nt': 
       
    _ = system('cls') 
    
  else: 
       
    _ = system('clear') 

def main2():

  console.print("What should I help you with?")
  console.print("\n")
  sleep(3)
  console.print("1.[red]Depression[/red]")
  console.print("2.[blue]Anxiety[/blue]")
  console.print("3.[green]Addictions[/green] and [green]Drugs[/green]")
  console.print("4.[magenta]Eating Disorders[/magenta]")
  
  print("\n")
  topics3=int(input("Enter a number:"))
  print("\n")
  if topics3 == 1:
    console.print("[blue]The mainstay of treatment is usually medication, talk therapy, or a combination of the two. Increasingly, research suggests these treatments may normalize brain changes associated with depression.[/blue]")
    sleep(10)

  if topics3 == 2:
    console.print("[green]Treatment includes counseling or medications, including antidepressants.[/green]")
    sleep(30)
  if topics3 == 3:
    console.print("[magenta]Exercise, Break the habit, Discover a new hobby, Love yourself, write down the harmful effects your alcohol or drug addiction has. Call for help – now.[/magenta]")
    sleep(30)
  if topics3 == 4:
    console.print("[red]1.Anorexia nervosa[/red]")
    console.print("2.Bulimia nervosa")
    console.print("3.Binge eating disorder")
    print("\n")
    topics4=int(input("Enter number:"))
    if(topics4==1):
      console.print("[red]Medical treatment may be needed to restore normal weight. Talk therapy can help with self-esteem and behavior changes.[/red]")
      sleep(30)
    if(topics4==2):
      console.print("[blue]Treatments include counseling, medications, and nutrition education.[/blue]")
      sleep(30)
    if(topics4==3):
      console.print("[yellow]Go for a Walk. Share on Pinterest. Sleep It Off. Eat a Healthy Breakfast. Stay Hydrated.[/yellow]")
      sleep(30)


