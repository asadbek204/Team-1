const inputs = document.querySelectorAll('.input-group input');

        inputs.forEach((input, index) => {
            input.addEventListener('input', (event) => {
                if (event.inputType === 'insertText') {
                    const enteredValue = parseInt(event.target.value);
                    if (!isNaN(enteredValue) && enteredValue >= 0 && enteredValue <= 9) {
                        if (index < inputs.length - 1 && event.target.value !== '') {
                            inputs[index + 1].focus();
                        } else if (index === inputs.length - 1 && event.target.value !== '') {
                            // Sizga kerak bo'lgan oxirgi son
                            const lastDigit = event.target.value;
                            console.log(`Oxirgi son: ${lastDigit}`);
                            // Boshqa amallarni bajaring, masalan, formani yuboring
                            // document.querySelector('form').submit();
                        }
                    } else {
                        // Foydalanuvchi noto'g'ri son kiritdi
                        event.target.value = '';
                    }
                }
            });
        });