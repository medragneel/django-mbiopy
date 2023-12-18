let element = document.querySelector('#container-01');
let config = {};
let viewer = $3Dmol.createViewer(element, config);
let pdbUri = 'static/6bb5.pdb';
jQuery.ajax(pdbUri, {
    success: function(data) {
        let v = viewer;
        v.addModel(data, "pdb");                       /* load data */
        v.setStyle({}, { cartoon: { color: 'spectrum' } });  /* style all atoms */
        v.zoomTo();                                      /* set camera */
        v.spin(true)
        v.render();                                      /* render scene */
    },
    error: function(hdr, status, err) {
        console.error("Failed to load PDB " + pdbUri + ": " + err);
    },
});

