export async function getData(url, arr, method = "GET") {
    const data = await fetch(url, {
      method: method,
    });
    const parsedData = await data.json();
  
    arr.push(...parsedData);
  
    return "HUCK";
  }