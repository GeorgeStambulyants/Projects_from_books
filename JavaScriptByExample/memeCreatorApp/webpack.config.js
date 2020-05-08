require('dotenv').config();
const webpack = require('webpack');

const isProduction = (process.env.NODE_ENV === 'production');

const PurifyCSSPlugin = require('purifycss-webpack');
const glob = require('glob');

const extractLess = new ExtractTextPlugin({
    filename: "[name].css",
});

module.exports = {
    context: __dirname,
    entry: {
        general: './src/js/general.js',
        memes: './src/js/memes.js',
    },
    output: {
        path: __dirname + '/dist',
        filename: '[name].js',
        publicPath: '/dist/',
    },
    devServer: {
        compress: true,
        port: 8080,
        hot: true,
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /(node_modules)/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['env', 'es2015'],
                    }
                }
            },
            {
                test: /\.(less|css)$/,
                use: extractLess.extract({
                    use: [
                        {
                            loader: 'style-loader'
                        },
                        {
                            loader: 'css-loader',
                            options: {
                                sourceMap: true
                            }
                        },
                        {
                            loader: 'less-loader',
                            options: {
                                sourceMap: true
                            }
                        }
                    ],
                    fallback: 'style-loader',
                })
            },
            {
                test: /\.(svg|eot|ttf|woff|woff2)$/,
                loader: 'url-loader',
                options: {
                    limit: 10000,
                    name: 'fonts/[name].[ext]'
                }
            },
            {
                test: /\.(png|jpg|gif)$/,
                loaders: [
                    {
                        loader: 'url-loader',
                        options: {
                            limit: 10000,
                            name: 'images/[name].[ext]'
                        }
                    },
                'img-loader'
                ],
            },
        ],
    },
    plugins: [
        new webpack.ProvidePlugin({
            $: 'jquery',
            jQuery: 'jquery',
            devtool: 'source-map',
        }),
        new webpack.HotModuleReplacementPlugin(),
        new webpack.DefinePlugin({
            ENVIRONMENT: JSON.stringify(process.env.NODE_ENV),
            CONSTANT_VALUE: JSON.stringify(process.env.CONSTANT_VALUE),
        }),
        extractLess,
        new PurifyCSSPlugin({
            paths: glob.sync(__dirname + '/*.html'),
            minimize: true,
        }),
    ],
}

if (isProduction) {
    module.exports.plugins.push(
        new webpack.optimize.UglifyJsPlugin({sourceMap: true})
    );
}
