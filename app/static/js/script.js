let fileForm = document.getElementById('fileForm')
let circlePlace = document.getElementById('circlePlace')
let circleText = document.getElementById('circleText')
let progressCircle = document.getElementById('progressCircle')

fileForm.addEventListener('submit', async function (event) {
    event.preventDefault(); // Останавливаем стандартную отправку формы
    circlePlace.style.display = 'flex'; // Показываем индикатор загрузки
    circleText.innerText = 'Пожалуйста подождите.'
    progressCircle.style.display = 'block'

    let formData = new FormData(fileForm);
    let fileName = fileForm.querySelector('input[type="file"]').files[0].name; // Получаем имя файла

    try {
        // Отправляем запрос и ждем ответа от сервера
        const response = await fetch(fileForm.action, {
            method: "POST",
            body: formData,
        });

        // Проверяем, что ответ успешный и возвращает файл
        if (!response.ok) {
            throw new Error("Ошибка при загрузке файла");
        }

        // Преобразуем ответ в Blob
        const blob = await response.blob();
        const downloadUrl = URL.createObjectURL(blob);

        // Создаем ссылку для скачивания файла с оригинальным именем
        const a = document.createElement("a");
        a.href = downloadUrl;
        a.download = fileName;  // Устанавливаем имя файла для скачивания
        document.body.appendChild(a);
        a.click();
        a.remove();  // Удаляем ссылку после клика

        URL.revokeObjectURL(downloadUrl);  // Очищаем URL
        
    } catch (error) {
        console.error("Произошла ошибка:", error);
    } finally {
        progressCircle.style.display = 'none'
        circleText.innerText = 'Готово, дождитесь загрузки.'
        circleText.style.paddingTop = '50px'
        setTimeout(() => {
            circlePlace.style.display = 'none'; // Прячем индикатор загрузки
        }, 2000)
    }
});
