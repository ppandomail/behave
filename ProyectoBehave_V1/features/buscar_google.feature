Feature: Buscar en Google

Scenario: Buscar AFIP en Google
    Given el usuario está en la página de Google
    When el usuario ingresa AFIP y pulsa tecla enter
    Then el usuario debería ver en el título de la página 'AFIP - Buscar con Google'