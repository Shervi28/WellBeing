from time import sleep
from os import system, name 
from rich.console import Console
from pyfiglet import Figlet, figlet_format

console = Console()

def clear4(): 
  
  if name == 'nt': 
       
    _ = system('cls') 
    
  else: 
       
    _ = system('clear') 

def main3():
  console.print("[red]What should I help you with?[/red]")
  console.print("\n")
  sleep(3)
  console.print("[blue]1.Muscle Pain[/blue]")
  console.print("[green]2.Bone Pain[/green]")
  console.print("[purple]3.Injuries[/purple]")
  console.print("4.Skin")
  
  print("\n")
  topics5=int(input("Enter a number:"))
  
  if topics5 == 1:
    console.print("1.[blue]tension[/blue]")
    console.print("2.[red]stress[/red]")
    console.print("3.[green]overuse[/green]")
    print("\n")
    topic6=int(input("Enter number:"))

    

  if topics5 == 2:
    console.print("[brown]1.Bone Fracture[/brown]")
    console.print("[brown]2.Joint Pain[/brown]")
    print("\n")
    topic6=int(input("Enter number:"))
    

  if topics5 == 3:
    console.print("[brown]1.Concussions[/brown]")
    console.print("[brown]2.Sprains[/brown]")
    console.print("[brown]3.Knee Injury[/brown]")
    print("\n")
    topic6=int(input("Enter number:"))

  if topics5 == 4:
    console.print("[brown]1.Sunburn[/brown]")
    console.print("[brown]2.Rashes[/brown]")
    console.print("[brown]3.Athletes Foot[/brown]")
    console.print("[brown]4.Warts[/brown]")
    print("\n")
    topic6=int(input("Enter number:"))
    print("\n")
  if(topics5==1 and topic6==1):
    console.print("[red]Treatments include pain relievers and other medications. Stress reduction, ice or heat on sore muscles, and good posture also may help[/red]")
    sleep(30)
  if(topics5==1 and topic6==2):
    console.print("[yellow]Exercise, Consider supplements, Light a candle, Reduce your caffeine intake[/yellow]")
    sleep(30)
  if(topics5==1 and topic6==3):
    console.print("[blue]Rest to allow the affected area the necessary time to heal[/blue]")
    sleep(30)
  if(topics5==2 and topic6==1):
    console.print("[magenta]Treatment often involves resetting the bone in place and immobilizing it in a cast or splint to allow it time to heal. Sometimes, surgery or metal rods may be needed to reset the bone.[/magenta]")
    sleep(30)
  if(topics5==2 and topic6==2):
    console.print("[blue]Use of heat, such as applying heating pads to aching joints, taking hot baths or showers, or immersing painful joints in warm paraffin wax, can help relieve pain temporarily.[/blue]")
    sleep(30)
  if(topics5==3 and topic6==1):
    console.print("[red]There's no specific cure for concussion. Rest and restricting activities allow the brain to recover. This means one should temporarily reduce sports, video games, TV, or too much socializing. Medications for headache pain, or odansetron or other anti-nausea medications can be used for symptoms.[/blue]")
    sleep(30)
  if(topics5==3 and topic6==2):
    console.print("[grey]Treatment varies and may include rest, ice, compression, and elevation (RICE) as well as anti-inflammatory medications.[/grey]")
    sleep(30)
  if(topics5==3 and topic6==3):
    console.print("[orange]Stop your activity immediately, Rest the joint at first, Reduce pain, swelling and internal bleeding with icepacks, applied for 15 minutes every couple of hours.[/orange]")
    sleep(30)
  if(topics5==4 and topic6==1):
    console.print("[magenta]Make frequent cool baths or showers to help relieve the pain. Use a moisturizer that contains aloe vera or soy to help soothe sunburned skin. Consider taking aspirin or ibuprofen to help reduce any swelling, redness and discomfort.[/magenta]")
    sleep(30)
  if(topics5==4 and topic6==2):
    console.print("[brown]Avoiding harsh soaps and detergents, perfumed soaps or lotions, and known allergy triggers may help soothe irritated skin. Using an over-the-counter antihistamine or steroid cream may also help.[/brown]")
    sleep(30)
  if(topics5==4 and topic6==3):
    console.print("[red]Treatment involves topical antifungal medications.[/red]")
    sleep(30)
  if(topics5==4 and topic6==4):
    console.print("[green]Treatment may include topical medications and removal through medical procedures.[/green]")
    sleep(30)
  else:
    clear4()

