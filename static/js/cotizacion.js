var elementos = [];
var listaDetalleHTML = document.getElementById('lista-detalle');
var total = 0.0;
var totalHTML = document.getElementById('total');

function agregarEnDetalle(event) {

    event.preventDefault();

    var listaProductos = document.querySelector('select');
    var cantidad = document.getElementById('cantidad').value;
    var precio = document.getElementById('precio').value;
    var listaSubtipos = document.getElementById('tipoProducto');
    var subtipo = listaSubtipos.options[listaSubtipos.selectedIndex].textContent;


    if ( listaProductos.selectedIndex == 0){
        return;
    }

    var subtotal = 0.0;

    var producto = {
        nombre: listaProductos.options[listaProductos.selectedIndex].textContent,
        subtotal: (cantidad * precio)
    };

    elementos.push(producto);
    total += producto.subtotal;
    var item = document.createElement('div');
    item.classList.add('mdl-list__item');
    var primaryContent = document.createElement('span');
    primaryContent.classList.add('mdl-list__item-primary-content');
    primaryContent.textContent = producto.nombre + ' tipo ' + subtipo;
    var secondaryContent = document.createElement('a');
    secondaryContent.classList.add('mdl-list__item-secondary-action');
    secondaryContent.textContent = '$' + Number.parseFloat(producto.subtotal).toFixed(2);

    item.appendChild(primaryContent);
    item.appendChild(secondaryContent);

    listaDetalleHTML.appendChild(item);
    totalHTML.textContent = Number.parseFloat(total).toFixed(2);
}

var subtipos;

function obtenerSubtipos() {

    var listaProductos = document.querySelector('select');
    var nombreProducto = listaProductos.options[listaProductos.selectedIndex].textContent;
    var listaSubtipos = document.getElementById('tipoProducto');

    var div = document.getElementById('abc');
    if (nombreProducto == 'Banner' || nombreProducto == 'Vinil') {
        div.style.display = 'inline';
    }else{
        div.style.display = 'none';
    }

    if (listaProductos.selectedIndex==0) {
        listaSubtipos.innerHTML = '<option>...</option>';
        return;
    }

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
           subtipos = JSON.parse(xhttp.responseText);
           listaSubtipos.innerHTML = '<option>Selecciona un tipo</option>';
           for (var i = 0; i < subtipos.length; i++) {
               var subtipo = subtipos[i];
               var option = document.createElement('option');
               option.value = subtipo.fields.producto;
               option.textContent = subtipo.fields.nombre;
               option.setAttribute('precio', subtipo.fields.precio);
               listaSubtipos.appendChild(option);
           }
        }
    };
    xhttp.open("GET", "/cotizacion/subconjunto/"+nombreProducto+"/", true);
    xhttp.send();
}

function obtenerPrecio() {
    var listaSubtipos = document.getElementById('tipoProducto');
    var subtipo = listaSubtipos.options[listaSubtipos.selectedIndex];
    var precio = document.getElementById('precio');
    precio.value = subtipo.getAttribute('precio');
    precio.focus();
}

function finalizar() {
    var datos = JSON.stringify(elementos);
    
}
