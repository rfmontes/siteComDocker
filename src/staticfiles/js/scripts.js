$(document).ready(function() {

    $("#id_cpf").mask("000.000.000-00")

    $("#id_cnpj").mask("00.000.000/0000-00")

    $("#id_telefone").mask("(00) 0000-00009")
    $("#id_telefone").blur(function(event){
        if ($(this).val().length == 15) {
            $("#id_telefone").mask("(00) 00000-0009")
        }else{
            $("#id_telefone").mask("(00) 0000-00009")
        }
    })

    $("#id_cep").mask("00000-000")

    var options = {
        translation: {
            'A': {pattern: /[A-Z]/},
            'B': {pattern: /[A-Z0-9]/}
        }
    }
    $("#id_placa").mask("AAA0B00", {
        translation: {
            'A': {pattern: /[A-Z]/},
            'B': {pattern: /[A-Z0-9]/}
        }
    })
})
