document.addEventListener('DOMContentLoaded', function () {
    // AJAX form submission for calculator
    const form = document.querySelector('form');
    const resultContainer = document.createElement('div');
    resultContainer.id = 'result-container';
    form.parentNode.insertBefore(resultContainer, form.nextSibling);

    form.addEventListener('submit', function (e) {
        e.preventDefault();
        const formData = new FormData(form);
        fetch('', {
            method: 'POST',
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
            },
            body: formData
        })
            .then(response => response.json())
            .then(data => {
                if (data.result) {
                    resultContainer.innerHTML = `
                    <h2>Result:</h2>
                    <ul>
                        <li>Total bushes: ${data.result.total_plants}</li>
                        <li>Total corn on the cob: ${data.result.total_cobs}</li>
                        <li>Estimated profit: $${data.result.total_income}</li>
                    </ul>
                `;
                } else if (data.errors) {
                    resultContainer.innerHTML = `<div style="color:red;">${data.errors}</div>`;
                } else {
                    resultContainer.innerHTML = '';
                }
            })
            .catch(() => {
                resultContainer.innerHTML = '<div style="color:red;">Error processing request.</div>';
            });
    });
});
