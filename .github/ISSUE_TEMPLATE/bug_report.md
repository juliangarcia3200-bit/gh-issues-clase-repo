name: Bug report
description: Reporta un error en el sistema contable
title: "[BUG] "
labels: ["bug"]
body:
  - type: textarea
    id: steps
    attributes:
      label: Pasos para reproducir
      description: Describe como reproducir el problema
      placeholder: |
        1. ...
        2. ...
        3. ...
    validations:
      required: true
  - type: textarea
    id: expected
    attributes:
      label: Comportamiento esperado
    validations:
      required: true
  - type: textarea
    id: actual
    attributes:
      label: Comportamiento actual
    validations:
      required: true
