# AES-nolib
Simple AES implementation without using any external library for Python3.x

<h1>Credits</h1>
First of all thanks to <a href="https://github.com/bonsaiviking">Daniel Miller</a> who created <a href=https://gist.github.com/bonsaiviking/5571001>this project</a> for python2

<h1>Usage</h1>
<h3>Imports:</h3>
<code>from AES import AES_128, make_blocks, block_check</code>
<br>
<h4>Functions:</h4>
<ul>
<li><code>block_check</code> - Creates the total block size multiple of 16 (Expects bytearray as parameter)</li>
<li><code>make_blocks</code> - Splits the block into chunks of size 16 (Expects bytearray block_check[ed] as parameter)</li>
<li><code>AES_128</code> - Main class of project used for encryption and decryption (Expects block of size 16 as parameter)</li>
</ul>

<h4><i>Can be directly tested by running test.py</i></h4>

<h3>Additional Notes</h3>
<p>This project is experimental and will be updated for AES-192 and AES-256 standards</p>
