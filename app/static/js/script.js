/**
 * Função valida os dados preenchidos pelo usário, com um array de objetos, com cada um sendo um campo com sua regra de validação
 * Percorrendo o array, limpa os espaços em branco no fim e começo dos campos
 * Caso algum campo esteja errado ele interrompe a função pedindo para que o usuário corrija
 */

function validarform(){

    const campos =[
         {id: "nome",nome:"Nome", regra: valor => valor !== ""},
         {id:"telefone",nome:"Telefone", regra: valor=> /^\d{2}9\d{8}$/.test(valor) },
         {id:"email",nome:"E-Mail",regra: valor => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(valor) },
         {id:"assunto",nome:"Assunto",regra: valor => valor !== "" }
    ];

    for(let campo of campos){

        const valor = document.getElementById(campo.id).value.trim();

        if(!campo.regra(valor)){
            alert(`Por favor, preencha corretamente o campo ${campo.nome}`);
            console.log(`${campo.nome} incorreto`)
            return false;
        }
    }
    
    return true;// Retorna true apenas se todos os campos forem válidos
}

async function enviarForm(dados) {  
    /* 
     * Função que envia os dados do form para o servidor
     * Recebe um objeto com os campos do form
     * Mostra menssagem de sucesso caso de tudo certo, ou alerta o usuário caso tenha alguma falha no envio.
    */
    // endpoint do servidor que recebe os dados (ajuste conforme necessário)
    const url = "http://localhost:5000/recieve_leads"
    try{
        const response = await fetch(url,  {
            method: "POST", 
            headers:{
                "Content-Type": "application/json"
            },
            body:JSON.stringify(dados)
        });

        if(!response.ok){
            throw new Error("Erro ao enviaro formulário");
        }

        const result = await response.json();
        console.log("Servidor:",result);
        alert("Enviado com sucesso! Entraremos em contato assim que possivel!");

    }catch(error){

        console.error("Erro:",error);
        alert("Ocorreu um erro ao enviar o formulário. Tente novamente mais tarde.");
    }
}
/**
 * Evento para esperar o html carregar completamente
 * Evento para quando o usuário apertar no enviar, todos os dados sejam validados e caso ok a função de enviar o formulário é chamada
 */

document.addEventListener("DOMContentLoaded",()=>{
    const form = document.getElementById("leadForm");

    form.addEventListener("submit", function(event){
        event.preventDefault();

        if(validarform()){

            console.log("Form enviado.");

            const dados ={
                nome: document.getElementById("nome").value.trim(),
                telefone: document.getElementById("telefone").value.trim(),
                email: document.getElementById("email").value.trim(),
                assunto: document.getElementById("assunto").value.trim()
            }
            
            enviarForm(dados);
        }

    });
});