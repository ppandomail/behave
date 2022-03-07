Feature: Buscar en Google

Scenario Outline: Buscar palabras en Google
    Given el usuario está en la página de Google
    When el usuario ingresa <palabra> y pulsa tecla enter
    Then el usuario debería ver en el título de la página '<palabra> - Buscar con Google'

Examples:
    | palabra    |
    | AFIP       |
    | BDD        |
    | AUTOMATION |