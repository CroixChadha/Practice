const fact_button = async () => {
    const response = await fetch ('https://catfact.ninja/fact');
    const myJson = await response.json();
}
fact_button.call()