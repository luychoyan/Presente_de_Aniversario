import flet as ft
import random

def main(page: ft.Page):
    page.title = 'Feliz Aniversário!'
    page.vertical_alignment = 'center'	
    page.horizontal_alignment = 'center'
    page.bgcolor = 'purple'
    page.window.width = 600
    page.window.height = 900
    page.window.min_width = 600
    page.window.min_height = 900
    page.window.max_width = 600
    page.window.max_height = 900
    
    background = ft.Image(
        src = 'assets/papel_de_parede.jpg',
        opacity= 0.7,
        fit= 'cover',
        width= '100%',
        height= '100%',
    )
    

    titulo = ft.Text('Feliz Animersário Meu Amor!', size= 35, color= 'white', weight= 'bold')

    # Aqui fica a lista de fotos
    fotos = [
        'Feliz_Aniversario/assets/foto2.jpg', 'Feliz_Aniversario/assets/foto3.jpg', 'Feliz_Aniversario/assets/foto4.jpg', 'Feliz_Aniversario/assets/foto7.jpg', 'Feliz_Aniversario/assets/foto8.jpg', 'Feliz_Aniversario/assets/foto10.jpg', 'Feliz_Aniversario/assets/foto11.jpg', 'Feliz_Aniversario/assets/foto12.jpg', 'Feliz_Aniversario/assets/foto13.jpg', 'Feliz_Aniversario/assets/foto14.jpg', 'Feliz_Aniversario/assets/foto15.jpg', 'Feliz_Aniversario/assets/foto17.jpg', 'Feliz_Aniversario/assets/foto18.jpg', 'Feliz_Aniversario/assets/foto19.jpg', 'Feliz_Aniversario/assets/foto20.jpg', 'Feliz_Aniversario/assets/foto21.jpg', 'Feliz_Aniversario/assets/foto22.jpg'
    ]
    fotos_index = 0

    # Aqui fica a lista de frases
    frases = [
        'Minha Princesinha!',
        'Minha Vida!',
        'Meu Tudo!',
        'Meu Mundo!',
        'Minha Gatinha!',
        'Minha deusa grega!',
        'Que Mulherão mds!',
        'Lindaaaaa! grrrr',
    ]

    frase_escolhida = ft.Text(value= 'Esse é meu presente para voce', size= 23, color= 'white')

    foto = ft.Image(
        src= fotos[fotos_index],
        height= 600,
        border_radius= 20,

    )

    def proxima_foto(e):
        # O nonlocal Acessa a variável fotos_index que está fora da função
        nonlocal fotos_index
        fotos_index = (fotos_index + 1) % len(fotos)
        foto.src = fotos[fotos_index]
        foto.update()

        nonlocal frase_escolhida
        frase_escolhida.value = random.choice(frases)
        frase_escolhida.update()
        
    def voltar_foto(e):
        # O nonlocal Acessa a variável fotos_index que está fora da função
        nonlocal fotos_index
        fotos_index = (fotos_index - 1) % len(fotos)
        foto.src = fotos[fotos_index]
        foto.update()

        nonlocal frase_escolhida	
        frase_escolhida.value = random.choice(frases)
        frase_escolhida.update()
     
    # Função para abrir o presente e mostrar o conteiner	
    def abrir_presente(e):
        conteiner.visible = True
        botao_abrir_presente.visible = False
        page.update()

    estilo_botao = ft.ButtonStyle(
        padding= 20,
        bgcolor= 'white',
        color= 'purple',
    )
    botao_proximo = ft.ElevatedButton(
        text= 'Proximo',
        on_click= proxima_foto,
        style= estilo_botao
    )

    botao_voltar = ft.ElevatedButton(
        text = 'Voltar',
        on_click= voltar_foto,
        style= estilo_botao
    )

    botoes = ft.Row([
            botao_voltar,
            botao_proximo
        ], 
        alignment= 'center',
        spacing= 50
    )

    caixa_principal = ft.Column([
            titulo,
            frase_escolhida,
            foto,
            botoes
        ],
        alignment= 'center', spacing= 20, horizontal_alignment= 'center'
    )

    conteiner = ft.Container(
        content= ft.Stack([
            background,
            caixa_principal
        ]),
        width= '100%',
        height= '100%',
        alignment= ft.alignment.center,
        visible= False
    )

    estilo_botao_presente = ft.ButtonStyle(
        padding= 20,
        bgcolor= 'white',
        color= 'purple',

    )
    botao_abrir_presente = ft.ElevatedButton(
        text= 'Abrir Presente',
        on_click= abrir_presente,
        style= estilo_botao_presente,
        width= 200,
        height= 100,
    )


    page.add(conteiner, botao_abrir_presente)

ft.app(main,)