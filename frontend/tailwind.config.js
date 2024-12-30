module.exports = {
  content: [
    './src/**/*.{html,js}',
    './node_modules/flowbite/**/*.js', // Include Flowbite's JS files
  ],
  theme: {
    extend: {
      colors: {
        beige: '#f5e9dc', // Soft beige for text
        'walnut-brown': '#4b2e2f', // Rich dark brown
        gold: '#d4af37', // Muted gold for accents
      },
    },
  },
  plugins: [
    require('flowbite/plugin'), // Add Flowbite's plugin
  ],
};
