from validations.menu_validation import Menu
menu = Menu()

process = input('Deseja iniciar a calculadora? S/N ')
process_validation = menu.process_validation(process) 

while process_validation:
    menu.show_menu()
    option = int(input('Escolha uma opção\n'))
    menu.option_validation(option) 
