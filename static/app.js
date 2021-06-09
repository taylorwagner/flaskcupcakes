const BASE_URL = "http://localhost:5000/api"


/** given data about a cupcake, generate HTML */
function generateCupcakeHTML(c) {
    return `
    <div data-cupcake-id=${c.id}>
    <li>
        ${c.flavor} / ${c.size} / ${c.rating}
        <button class="delete-button btn btn-danger">X</button>
    </li>
    <img class="Cupcake-img" src="${c.image}"
    alt="(no image provided)">
    </div>`;
}

async function showCupcakes() {
  // Make an ajax request to the Cupcakes api to put initial Cupcakes on page

  const res = await axios.get(`${BASE_URL}/cupcakes`);

  for (let cData of res.data.cupcakes) {
      let newCupcake = $(generateCupcakeHTML(cData));
      $('#all-cupcakes').append(newCupcake);
  }
}


/** handle form for adding new cupcakes */

// $("#new-cupcake-form").on("submit", async function (e) {
//     e.preventDefault();
  
//     let flavor = $("#form-flavor").val();
//     let rating = $("#form-rating").val();
//     let size = $("#form-size").val();
//     let image = $("#form-image").val();

//     const newCupcakeResponse = await axios.post(`${BASE_URL}/cupcakes`, {
//         flavor,
//         rating,
//         size,
//         image
//     });

//     let newCupcake = $(generateCupcakeHTML(newCupcakeResponse.data.cupcake));
//     $("#all-cupcakes").append(newCupcake);
//     $("#new-cupcake-form").trigger("reset");
// });


/** handle clicking delete: delete cupcake */

$("#all-cupcakes").on("click", ".delete-button", async function (e) {
    e.preventDefault();
    let $cupcake = $(e.target).closest("div");
    let cupcakeId = $cupcake.attr("data-cupcake-id");
  
    await axios.delete(`${BASE_URL}/cupcakes/${cupcakeId}`);
    $cupcake.remove();
});

$(showCupcakes);