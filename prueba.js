const axios = require('axios');

const ipAddress = '44.229.200.200'; 

axios.get(`http://${ipAddress}`)
  .then(response => {
    console.log('Response data:', response.data);
  })
  .catch(error => {
    console.error('Error:', error.message);
  });
