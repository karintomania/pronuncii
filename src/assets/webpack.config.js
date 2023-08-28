const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
  entry: {
    index: './js/index.js',
    sass: './sass/index.sass',
  },  // path to our input file
  output: {
    filename: '[name]-bundle.js',  // output bundle file name
    path: path.resolve(__dirname, '../static'),  // path to our Django static directory
  },
  plugins: [
        new MiniCssExtractPlugin({
            filename: 'styles.css' // Specify the name of the generated CSS file
        })
    ],
  module: {
    rules: [
      {
        test: /\.sass$/i,
        use: [
            MiniCssExtractPlugin.loader,
            'css-loader',
            'sass-loader',
        ],
      },
    ],
  },
};
