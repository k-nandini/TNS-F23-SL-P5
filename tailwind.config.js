/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*"], // Location of HTML to watch
  theme: {
    extend: {
      fontFamily: {
        'sans': ['Verdana', 'sans'], // Add Verdana to the sans-serif font family
      },
    },
  },
  plugins: [],
}