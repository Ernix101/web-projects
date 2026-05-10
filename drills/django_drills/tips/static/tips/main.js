let currentForm = null;

document.querySelectorAll('.delete-form button').forEach(button => {
    button.addEventListener('click', function(e) {
        e.preventDefault();
        currentForm = this.closest('form');
        document.getElementById('Modal').style.display = 'block';
    });
});

document.getElementById('confirmDelete').addEventListener('click', function() {
    if (currentForm) currentForm.submit();
});

function closeModal() {
    document.getElementById('Modal').style.display = 'none';
    currentForm = null;
}