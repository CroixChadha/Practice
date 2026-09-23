function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}
// function for the one cat fact button
window.onload = function() {
const fact = document.querySelector('.resultarea')
const factbutton = document.querySelector('.fact')
const getOneCatFact = async () => {
    try{
        const res = await fetch('https://catfact.ninja/fact')

        const data = await res.json();
        fact.textContent = data.fact
    } catch(e) {
        console.error(e)
    }   
    
}
factbutton.addEventListener('click', () => {
    getOneCatFact()
})


//function for the facts one. 

const facts = document.querySelector('.resultarea')
const factsbutton = document.querySelector('.facts')
const getCatFacts = async () => {
    try{
        const res = await fetch('https://catfact.ninja/facts?page=' + getRandomInt(34))

        const data = await res.json();
        facts.textContent = data.data
        console.log(data)
    } catch(e) {
        console.error(e)
    }   
    
}
factsbutton.addEventListener('click', () => {
    getCatFacts()
})
}