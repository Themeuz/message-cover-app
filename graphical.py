import flet as ft

def main(pagina):
    titulo = ft.Text("Receitinha Discord")

    nome_usuario = ft.TextField(label="Escreva seu nome aqui")

    chat = ft.Column()
    def enviar_mensagem_tunel(informacoes):
        chat.controls.append(ft.Text(informacoes))

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        texto_campo_mensagem = f"{nome_usuario.value}: {campo_mensagem.value}"

        pagina.pubsub.send_all(texto_campo_mensagem)
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label="Escreva sua mensagem aqui", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    def entrar_chat(evento):
        if not nome_usuario.value:
            nome_usuario.error_text = "Nome não cadastrado"
            nome_usuario.update()
        else:
            pagina.session.set("nome_usuario", nome_usuario.value)
            popup.open = False
            pagina.remove(botao_iniciar)
            pagina.remove(botao_entrar)
            pagina.add(chat)
            linha_mensagem = ft.Row([campo_mensagem, botao_enviar])
            pagina.add(linha_mensagem)
            texto = f"{nome_usuario.value} entrou no chat"
            chat.controls.append(ft.Text(texto))
            avatar = ft.CircleAvatar(nome_usuario.value[0].upper(), radius=20, bg_color="#3498db", text_color="#ffffff")
            pagina.add(avatar)
            linha_mensagem = ft.Row([campo_mensagem, botao_enviar])
            pagina.add(linha_mensagem)
            texto = f"{nome_usuario.value} entrou no chat"
            chat.controls.append(ft.Text(texto))
            pagina.update()
            pagina.update()

    popup = ft.AlertDialog(
        open=True,
        modal=True,
        title=ft.Text("Registre sua conta"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_chat)]
    )

    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Registrar", on_click=iniciar_chat)
    botao_entrar = ft.ElevatedButton("Entrar", disabled=True)

    pagina.add(titulo)
    pagina.add(botao_iniciar)
    pagina.add(botao_entrar)
    pagina.update()

ft.app(main)