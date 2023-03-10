const pedirAlumnos = async () => {
    const respuesta = await fetch("http://localhost:alumnos" , {
        method: "GET",

});

const data = await respuesta.json();

console.log(data);
};
pedirAlumnos()
