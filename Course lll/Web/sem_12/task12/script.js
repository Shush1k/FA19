class Square {
    constructor(name, lat, lon, address, area) {
        this.name = name;
        this.lat = lat;
        this.lon = lon;
        this.address = address;
        this.area = area
    }
    showInfo() {
        return "<b>"+this.name+"</b><br>"+this.address
    }

}

async function dataInit(){

    let squareArr=[];
    for (let i=0;i<data.length; i++){

        let name = data[i]["ObjectName"];
        let coords = data[i]["geoData"]["coordinates"];
        let address = data[i]["Address"];
        let area = data[i]["AdmArea"]
        let square = new Square(name, coords[1], coords[0], address, area)
        squareArr.push(square);
    }

    return squareArr;
}

async function statsCounter(dataArray) {

    let stat = new Map();

    for (let i = 0; i < dataArray.length; i++) {
        let area = dataArray[i].area;
        if (area === undefined){
            continue
        }

        if (stat.has(area) === false){
            stat.set(area, 0);
        }

        stat.set(area, stat.get(area) + 1);
    }

    return new Map([...stat.entries()].sort((a, b) => b[1] - a[1]));
}

async function tableStats() {

    let squareArr = await dataInit();

    let stats = await statsCounter(squareArr);

    let returnStr = '<table class="table"><thead><tr><th scope="col">№</th><th scope="col">Округ</th><th scope="col">Кол-во площадок</th></tr></thead><tbody>'
    let bufferCounter = 0;
    for (let [key, value] of stats) {
        returnStr += '<tr> <th scope="row">'+bufferCounter+'</th><td>' + key + '</td> <td>' + value + '</td></tr>';
        bufferCounter++;
    }
    returnStr += ' </tbody></table>'
    document.getElementById("mytable").innerHTML = returnStr;
}


async function dataFiller(){
    let squareArr = await dataInit();

    let map = L.map('map').setView({lat: 55.75343329146573, lon: 37.61715415648654}, 10);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19, attribution: '&copy; <a href="https://openstreetmap.org/copyright">OpenStreetMap contributors</a>'
    }).addTo(map);

    L.control.scale().addTo(map);

    for (let i=0; i<squareArr.length; i++){
        console.log(squareArr[i].showInfo())
        L.marker({lon: squareArr[i].lon, lat: squareArr[i].lat}).bindPopup(squareArr[i].showInfo()).addTo(map);
        // не работает в safari
        // https://stackoverflow.com/questions/65369083/popup-does-not-open-when-clicking-on-marker-safari/65369228
    }

}