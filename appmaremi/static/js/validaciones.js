//validacion login
function submitForm1() {
  var email2 = document.getElementById('exampleInputEmail1').value; //esta línea obtiene el valor ingresado del campo y lo guarda en la variable email2.

  var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;//, verifica que la cadena tenga un formato típico de dirección de correo electrónico
  
  if (!emailRegex.test(email2)) {
    alert('Por favor, ingrese un correo electrónico válido.');
    return;
  /* este bloque de código muestra una alerta al usuario si la dirección de correo electrónico ingresada 
  no cumple con el formato especificado por la expresión regular.*/
  }


  $('#successModal').modal('show');/*esta línea de código muestra el modal de éxito en la página web 
  al seleccionar el elemento con ID "successModal" y aplicar la función que lo hace visible.*/
}

function redirigirAIndex() {
  
  window.location.href = 'index.html';
}

    // Fin de la validación de inicio de sesión
    
    
    //validacion contacto

function submitForm3() {
  // 
  var nombre = document.getElementById('nombre').value;
  var email = document.getElementById('email').value;
  var telefono = document.getElementById('telefono').value;
  var direccion = document.getElementById('direccion').value;

  // validacion de nombre vacio
  if (nombre.trim() === '') {
    alert('Por favor, ingrese su nombre.');
    return;
  }

  // Validacion de gmail
  var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    alert('Por favor, ingrese un correo electrónico válido.');
    return;
  }

  // Validacion de numero (8 digitos)
  var telefonoRegex = /^[0-9]{8}$/;
  if (!telefonoRegex.test(telefono)) {
    alert('Por favor, ingrese un número de teléfono válido (8 dígitos).');
    return;
  }

  if (direccion.trim() === '') {
    alert('Por favor, ingrese su Direccionnombre.');
    return;
  }

  // modal
  $('#successModal').modal('show');
}

function limpiarFormulario() {
  //limpiar formulario
  document.getElementById('nombre').value = '';
  document.getElementById('email').value = '';
  document.getElementById('telefono').value = '';
  document.getElementById('direccion').value = '';
  document.getElementById('mensaje').value = '';
}


//Fin de la validacion contacto