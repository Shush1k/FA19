// https://is.gd/Y2fugK
// OR
// https://tinyurl.com/3r6nyf6r
$(function() {
    // https://stackoverflow.com/questions/14267781/sorting-html-table-with-javascript
    // get cell value from table row
    const getCellValue = (tr, idx) => tr.children[idx].innerText || tr.children[idx].textContent;

    const comparer = (idx, asc) => (a, b) => ((v1, v2) =>
        v1 !== '' && v2 !== '' && !isNaN(v1) && !isNaN(v2) ? v1 - v2 : v1.toString().localeCompare(v2)
    )(getCellValue(asc ? a : b, idx), getCellValue(asc ? b : a, idx));

    // for each tr do this
    document.querySelectorAll('th').forEach(th => th.addEventListener('click', () => {
        const table = th.closest('table'); // choice the table for filling
        Array.from(table.querySelectorAll('tr:nth-child(n+2)')) // all table rows without header (n+2)
            .sort(comparer(Array.from(th.parentNode.children).indexOf(th), this.asc = !this.asc))
            .forEach(tr => table.appendChild(tr)); // change the value

    }));

    // selected row 
    document.querySelectorAll('th').forEach(th => th.addEventListener('click', () => {
        var arr = Array.from(table.querySelectorAll('tr:nth-child(n)'));
        arr = Array.prototype.slice.call(arr[0].children);
        arr.forEach((th) => { th.classList.remove("th-selected"); })
        th.classList.add("th-selected");
    }));
});