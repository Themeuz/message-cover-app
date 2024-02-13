import flet as ft

# ------------------------------------
# Estilos Globais:
# ------------------------------------

# Estilo comumente usado para links
link_style = {
    "height": 50,
    "focused_border_color": "#FFFFF",
    "border_radius": 5,
    "cursor_height": 16,
    "cursor_color": "white",
    "content_padding": 10,
    "border_width": 1.5,
    "text_size": 14,
    "label_style": ft.TextStyle(color="#C08497"),
}
# ------------------------------------
# Classe: Link:
# ------------------------------------
# Define a classe Link...
class Link(ft.TextField):
    """Componente de link personalizável que mostra um Snackbar na seleção."""

    def __init__(self, label: str, value: str, page: ft.Page):
        """Cria um novo Link.

        Args:
            label (str): Texto exibido como label do link.
            value (str): Valor copiado na seleção.
            page (ft.Page): Página em que o link está inserido.
        """
        super().__init__(
            value=value, read_only=True, label=label, on_focus=self.selected, **link_style
        )
        self.page = page

    def selected(self, event: ft.TapEvent = None):
        """Mostra um Snackbar ao selecionar o link."""
        self.page.snack_bar = ft.SnackBar(
            ft.Text(f"Copied {self.label}!"), show_close_icon=True, duration=2000
        )
        self.page.snack_bar.open = True
        self.page.update()

# Define a página de perfil...
class ProfilePage(ft.View):

    # ...

    controls = [
        # ...
        ft.Column(
            spacing=20,
            controls=[
                # Insira os itens de texto aqui...
                TextField(
                    label="Nome",
                    value="",
                    text_size=14,
                    border_radius=5,
                    border_color="#C08497",
                    padding=ft.padding.only(left=10, right=10),
                ),
                TextField(
                    label="Senha",
                    value="",
                    password=True,
                    text_size=14,
                    border_radius=5,
                    border_color="#C08497",
                    padding=ft.padding.only(left=10, right=10),
                ),
                TextField(
                    label="Email",
                    value="",
                    text_size=14,
                    border_radius=5,
                    border_color="#C08497",
                    padding=ft.padding.only(left=10, right=10),
                ),
            ],
        ),
    ]


# Define a página inicial...
class LandingPage(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(route="/landing", padding=60)
        self.page = page
        self.lock = ft.Icon(name="lock", scale=ft.Scale(4))
        self.button = ft.Container(
            border_radius=5,
            expand=True,
            bgcolor="#C08497",
            content=ft.Text("Check Linkage", color="black", size=18),
            padding=ft.padding.only(left=25, right=25, top=10, bottom=10),
            alignment=ft.alignment.center,
            on_click=None,
        )

        self.controls = [
            ft.SafeArea(
                expand=True,
                content=ft.Column(
                    alignment="spaceBetween",
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Divider(height=120, color="transparent"),
                                self.lock,
                                ft.Divider(height=70, color="transparent"),
                                ft.Text(
                                    "Não sei",
                                    size=18,
                                    text_align="center",
                                ),
                            ],
                            horizontal_alignment="center",
                        ),
                        ft.Row(controls=[self.button], alignment="center"),
                    ],
                ),
            )
        ]

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK

    def router(route):
        page.views.clear()

        if page.route == "/landing":
            landing = LandingPage(page)
            page.views.append(landing)

        if page.route == "/profile":
            profile = ProfilePage(page)
            page.views.append(profile)

        page.update()

    page.on_route_change = router
    page.go("/profile")

ft.app(target=main, assets_dir="assets")
