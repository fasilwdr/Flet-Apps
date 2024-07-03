import uuid
import hashlib
import platform
import flet as ft



def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    device_id_text = ft.Text("", text_align=ft.TextAlign.CENTER)

    def get_device_id(e):
        # Gather hardware information
        system = platform.system()
        node = platform.node()
        processor = platform.processor()
        machine = platform.machine()

        # Combine information to form a unique string
        hardware_info = f"{system}-{node}-{processor}-{machine}"

        # Generate a UUID based on the hardware information
        hardware_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, hardware_info)

        # Hash the UUID to get a fixed-length unique ID
        device_id = hashlib.sha256(hardware_uuid.bytes).hexdigest()
        device_id_text.value = device_id
        device_id_text.update()

    page.add(
        ft.Column(
            [
                device_id_text,
                ft.ElevatedButton("Get Device ID", on_click=get_device_id),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(main)