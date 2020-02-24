function getUnique(s) {
  return [...new Set(s.split("\n"))].join("\n")

}

start.onclick = () => {
  strings.value = getUnique(strings.value)
  var c = textarea.value
  c = make_download(c)

}

	let file_name = 'Result.txt';
const textarea = document.getElementById('strings');
// editor = CKEDITOR.replace(textarea);
const files = document.getElementById('files');

// Прочесть файл
function read_file(file) {
    const reader = new FileReader();
    reader.onload = () => {
        const text = reader.result;
        textarea.value = text;
        make_download(text, file.name);
    };
    reader.readAsText(file);
}

// Вешаем обработчики
files.addEventListener('change', () => {
    read_file(files.files[0]);
    file_name = files.files[0].name;
}, false);



// Создать файл
function generate_file(data){
    data = new Blob(["\ufeff", [data]], {type:'plain/text'});
    return window.URL.createObjectURL(data);
}


// Создание ссылки для скачивания
function make_download(content, name = file_name){
    const download_link = document.getElementById('file');
    download_link.innerText = name;
    download_link.download = name;
    download_link.href = generate_file(content);
}


