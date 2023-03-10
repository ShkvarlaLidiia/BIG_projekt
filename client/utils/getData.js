export async function getData(url, metod = "GET") {
    const data = await fetch(url, {
        metod: metod,
    });
    const parsedData = await data.json()
    console.log(parsedData);
}
