# static.py

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>DaViDoNe</title>
    <link rel="icon" href="https://images.emojiterra.com/twitter/v14.0/1024px/1f1ee-1f1f9.png" type="image/x-icon">
    <title>Fast Search Example</title>
    <style>
        * {
            box-sizing: border-box;
        }
        body, html {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            font-size: 2.2vh;
            font-family: 'Open Sans', Arial, sans-serif;
            color: white;
            background: url('https://png.pngtree.com/png-clipart/20220823/ourlarge/pngtree-italian-flag-brush-png-image_6118954.png') center center repeat;
            background-size: cover;
            display: flex;
            align-items: flex-start;
            justify-content: center;
            overflow-y: auto;
        }
        #addon {
            background: rgba(0, 0, 0, 0.8);
            padding: 0.5vh;
            border-radius: 10px;
            width: 65vh;
            max-width: 100%;
            text-align: center;
            margin-top: 10vh;
        }
        .logo {
            width: 12vh;
            margin: 0 auto;
            margin-bottom: 3vh;
            margin-top: -3vh;
        }
        .logo img {
            width: 100%;
            height: auto;
        }
        h1, h2, h3 {
            margin: 0;
            text-shadow: 0 0 1vh rgba(0, 0, 0, 0.15);
        }
        h1 {
            font-size: 4.5vh;
            font-weight: 700;
        }
        h2 {
            font-size: 2vh;
            font-weight: normal;
            font-style: italic;
            opacity: 0.8;
            margin-bottom: 20px;
        }
        h3 {
            font-size: 2.2vh;
            margin-bottom: 10px;
        }
        .contact {
            position: absolute;
            left: 0;
            bottom: 4vh;
            width: 100%;
            text-align: center;
        }
        .contact a {
            font-size: 1.4vh;
            font-style: italic;
        }
        .button-container {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        button {
            border: 0;
            outline: 0;
            color: white;
            background: #8A5AAB;
            padding: 1.2vh 3.5vh;
            text-align: center;
            font-family: 'Open Sans', Arial, sans-serif;
            font-size: 2.2vh;
            font-weight: 600;
            cursor: pointer;
            display: block;
            box-shadow: 0 0.5vh 1vh rgba(0, 0, 0, 0.2);
            transition: box-shadow 0.1s ease-in-out;
            width: 80%;
            max-width: 35vh;
            margin: 1vh auto;
        }
        button:hover {
            box-shadow: none;
        }
        button:active {
            box-shadow: 0 0 0 0.5vh white inset;
        }
        #manifestBox {
            margin-top: 2vh;
            padding: 2vh;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 5px;
            display: none;
            text-align: left;
            white-space: pre-wrap;
        }
        #generateManifestButton {
            background: #4CAF50;
            margin-bottom: 1vh; /* Add space between buttons */
        }
        #installButton {
            background: #FF5722;
        }
        #installButton a {
            color: white;
            text-decoration: none;
        }
        #additionalText {
            margin-top: 2vh;
            font-size: 1.8vh;
            text-align: center; /* Center align the text */
        }
        @media (max-width: 600px) {
            .provider-group label {
                font-size: 2vh;
                white-space: nowrap;
            }
        }
    </style>
</head>
<body>
    <div id="addon">
        <div class="logo">
            <img src="https://images.emojiterra.com/twitter/v14.0/1024px/1f1ee-1f1f9.png" alt="Logo">
        </div>
        <h1 class="name">DaViDoNe</h1>
        <h2 class="version">Versione Beta 0.0.1</h2>
        <div id="additionalText">
            <h2>Minimal con 2 soli tasti</h2>
        </div>
        <p class="description">Già preconfigurato con MediaFlow Proxy e LiveTV</p>
        <form class="pure-form" id="provider-form">
        </form>
        <div class="button-container">
            <button id="generateManifestButton">Visualizza manifesto json</button>
            <div id="manifestBox"></div>
            <button id="installButton">Installa su Stremio</button>
        </div>
    </div>
    <script>
    // Function to generate the manifest URL
    function generateManifest() {
        let manifest = "|";
        const providers = {
            "streamingcommunity": "SC",
            "lordchannel": "LC",
            "streamingwatch": "SW",
            "animeworld": "AW",
            "filmpertutti": "FT",
            "cb01": "CB",
            "ddlstream": "DDL",
            "livetv": "LIVETV",
            "mediaflowproxy": "MFP"
        };

        // Add selected providers to the manifest
        for (const id in providers) {
            if (id === "mediaflowproxy") {
                // Add proxy details
                const proxyUrl = "https://tipotoko-spacemfpx.hf.space";
                const proxyPassword = "Password";
                manifest += `MFP[${proxyUrl},${proxyPassword}]|`;
            } else {
                manifest += providers[id] + "|";
            }
        }

        const instanceUrl = "{instance_url}"; // Replace with your instance URL
        const manifestUrl = instanceUrl + "/" + manifest + "/" + "manifest.json";
        return manifestUrl;
    }

    // Toggle manifest visibility and button text
    document.getElementById('generateManifestButton').addEventListener('click', function() {
        const manifestBox = document.getElementById("manifestBox");
        const button = document.getElementById('generateManifestButton');
        if (manifestBox.style.display === "none" || manifestBox.style.display === "") {
            const manifestUrl = generateManifest();
            manifestBox.style.display = "block";
            manifestBox.innerText = manifestUrl;
            button.innerText = "Nascondi manifesto json";
        } else {
            manifestBox.style.display = "none";
            button.innerText = "Visualizza manifesto json";
        }
    });

    // Install the manifest in Stremio
    document.getElementById('installButton').addEventListener('click', function() {
        let manifestUrl = generateManifest();
        manifestUrl = manifestUrl.replace("http://", "");
        manifestUrl = manifestUrl.replace("https://", "");
        const stremioUrl = "stremio://" + manifestUrl;
        window.location.href = stremioUrl;
    });
    </script>
</body>
</html>
"""
