function mostrarError(campo, mensaje) {
    campo.classList.add('is-invalid');
    campo.classList.remove('is-valid');

    let aviso = campo.parentElement.querySelector('.js-error');
    if (!aviso) {
        aviso = document.createElement('div');
        aviso.className = 'js-error text-danger small';
        campo.parentElement.appendChild(aviso);
    }
    aviso.textContent = mensaje;
}

function limpiarError(campo) {
    campo.classList.remove('is-invalid');
    campo.classList.add('is-valid');

    const aviso = campo.parentElement.querySelector('.js-error');
    if (aviso) {
        aviso.remove();
    }
}

function activarValidacion(formId, reglas) {
    const form = document.getElementById(formId);
    if (!form) {
        return;
    }

    function validarCampo(regla) {
        const campo = document.getElementById(regla.id);
        const mensaje = regla.validar(campo.value.trim());

        if (mensaje) {
            mostrarError(campo, mensaje);
            return false;
        }
        limpiarError(campo);
        return true;
    }

    reglas.forEach(function (regla) {
        const campo = document.getElementById(regla.id);
        campo.addEventListener('input', function () {
            validarCampo(regla);
        });
        campo.addEventListener('change', function () {
            validarCampo(regla);
        });
    });

    form.addEventListener('submit', function (event) {
        let todoBien = true;

        reglas.forEach(function (regla) {
            if (!validarCampo(regla)) {
                todoBien = false;
            }
        });

        if (!todoBien) {
            event.preventDefault();
            const primerError = form.querySelector('.is-invalid');
            if (primerError) {
                primerError.focus();
            }
        }
    });
}

const reglasProducto = [
    {
        id: 'id_nombre',
        validar: function (valor) {
            if (valor === '') {
                return 'El nombre es obligatorio.';
            }
            if (valor.length < 3) {
                return 'El nombre debe tener al menos 3 caracteres.';
            }
            return '';
        }
    },
    {
        id: 'id_descripcion',
        validar: function (valor) {
            if (valor.length > 500) {
                return 'La descripción no puede superar los 500 caracteres.';
            }
            return '';
        }
    },
    {
        id: 'id_precio',
        validar: function (valor) {
            if (valor === '') {
                return 'El precio es obligatorio y debe ser un número.';
            }
            if (Number(valor) <= 0) {
                return 'El precio debe ser mayor que cero.';
            }
            return '';
        }
    },
    {
        id: 'id_cantidad_disponible',
        validar: function (valor) {
            if (valor === '') {
                return 'La cantidad es obligatoria y debe ser un número.';
            }
            const numero = Number(valor);
            if (!Number.isInteger(numero) || numero < 0) {
                return 'La cantidad debe ser un número entero igual o mayor que cero.';
            }
            return '';
        }
    }
];

const reglasPedido = [
    {
        id: 'id_numero_pedido',
        validar: function (valor) {
            if (valor === '') {
                return 'El número de pedido es obligatorio.';
            }
            return '';
        }
    },
    {
        id: 'id_cliente',
        validar: function (valor) {
            if (valor === '') {
                return 'El nombre del cliente es obligatorio.';
            }
            return '';
        }
    },
    {
        id: 'id_descripcion',
        validar: function (valor) {
            if (valor === '') {
                return 'La descripción del pedido es obligatoria.';
            }
            return '';
        }
    },
    {
        id: 'id_valor_total',
        validar: function (valor) {
            if (valor === '') {
                return 'El valor total es obligatorio y debe ser un número.';
            }
            if (Number(valor) <= 0) {
                return 'El valor total debe ser mayor que cero.';
            }
            return '';
        }
    },
    {
        id: 'id_estado',
        validar: function (valor) {
            const permitidos = ['pendiente', 'confirmado', 'cancelado'];
            if (!permitidos.includes(valor)) {
                return 'Selecciona un estado válido.';
            }
            return '';
        }
    }
];