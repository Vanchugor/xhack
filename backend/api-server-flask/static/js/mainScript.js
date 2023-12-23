document.addEventListener("DOMContentLoaded", function () {

    document.getElementById('uploadForm').addEventListener('submit', function (event) {
        event.preventDefault();

        var form = event.target;
        var formData = new FormData(form);

        fetch(form.action, {
            method: 'POST',
            body: formData
        })
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
                var resultsDiv = document.getElementById('results');
                var imageContainer = document.getElementById('imageContainer');
                var prevBtn = document.getElementById('prevBtn');
                var nextBtn = document.getElementById('nextBtn');
                var currentImageIndex = 0;

                prevBtn.addEventListener('click', function () {
                    if (currentImageIndex > 0) {
                        currentImageIndex--;
                        showImage(currentImageIndex);
                    }
                });

                nextBtn.addEventListener('click', function () {
                    if (currentImageIndex < data['corrected_images'].length - 1) {
                        currentImageIndex++;
                        showImage(currentImageIndex);
                    }
                });

                function showImage(index) {
                    var imageUrl = data['corrected_images'][index];
                    var img = document.createElement('img');
                    img.classList.remove('run-animation');
                    img.classList.add('run-animation');
                    img.onload = function () {
                        var maxWidth = 800;
                        var maxHeight = 800;
                        var width = img.width;
                        var height = img.height;

                        if (width > maxWidth || height > maxHeight) {
                            var scaleFactor = Math.min(maxWidth / width, maxHeight / height);
                            width *= scaleFactor;
                            height *= scaleFactor;
                        }

                        img.width = width;
                        img.height = height;
                    };
                    img.src = imageUrl;
                    imageContainer.innerHTML = '';
                    imageContainer.appendChild(img);
                }

                showImage(currentImageIndex);
                document.getElementById('prevBtn').style.opacity = "100%";
                document.getElementById('nextBtn').style.opacity = "100%";
                /*resultsDiv.innerHTML = '';
                data['corrected_images'].forEach(function (imageUrl) {
                    var img = document.createElement('img');
                    img.onload = function () {
                        var maxWidth = 800;
                        var maxHeight = 800;
                        var width = img.width;
                        var height = img.height;

                        if (width > maxWidth || height > maxHeight) {
                            var scaleFactor = Math.min(maxWidth / width, maxHeight / height);
                            width *= scaleFactor;
                            height *= scaleFactor;
                        }

                        img.width = width;
                        img.height = height;
                    };
                    img.src = imageUrl;
                    resultsDiv.appendChild(img);
                });*/
                // demo1 = createBvambient()
            })
            .catch(function (error) {
                console.log(error);
            });
    });

    var demo1 = createBvambient()
});

function createBvambient() {
    return new Bvambient({
        selector: "#ambient",
        fps: 60,
        max_transition_speed: 12000,
        min_transition_speed: 8000,
        particle_number: 30,
        particle_maxwidth: 60,
        particle_minwidth: 10,
        particle_radius: 50,
        particle_opacity: true,
        particle_colision_change: true,
        particle_background: "#58c70c",
        particle_image: {
            image: false,
            src: ""
        },
        responsive: [
            {
                breakpoint: 768,
                settings: {
                    particle_number: "15"
                }
            },
            {
                breakpoint: 480,
                settings: {
                    particle_number: "10"
                }
            }
        ]
    });
}