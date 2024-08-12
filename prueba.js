const axios = require('axios');

const ipAddress = 'quintoproyecto.onrender.com'; 

axios.get(`http://${ipAddress}`)
  .then(response => {
    console.log('Response data:', response.data);
  })
  .catch(error => {
    console.error('Error:', error.message);
  });
