// SCRIPTS ALERT DELETE
document.addEventListener("DOMContentLoaded", function() {
    const deleteButtons = document.querySelectorAll(".delete-button");

    deleteButtons.forEach(button => {
        button.addEventListener("click", function(event) {
            event.preventDefault(); // Mencegah tautan langsung dijalankan
            
            const deleteUrl = this.getAttribute("href"); // Ambil URL untuk penghapusan

            Swal.fire({
                title: "Apakah Anda yakin?",
                text: "Produk ini akan dihapus secara permanen!",
                icon: "warning",
                showCancelButton: true,
                confirmButtonColor: "#success",
                cancelButtonColor: "#d33",
                confirmButtonText: "Delete!",
                cancelButtonText: "Cancel"
            }).then((result) => {
                if (result.isConfirmed) {
                    window.location.href = deleteUrl; // Lanjutkan ke URL penghapusan
                }
            });
        });
    });
});
