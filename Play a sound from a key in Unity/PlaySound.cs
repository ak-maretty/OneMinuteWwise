using System.Collections;
using System.Collections.Generic;
using UnityEngine;
 
public class PlaySound : MonoBehaviour
{
    // 'public'             Access Modifier that allows the property to be visible in the Inspector.
    // 'AK.Wwise.Event'     Wwise Type property.
    // 'SomeSound'          Name of the property.
    // ';'                  Declared as the end of line.
    public AK.Wwise.Event SomeSound;
 
    // Start is called before the first frame update
    void Start()
    {
       
    }
 
    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space)) {
            // SomeSound    Name of property.
            // Post()       Post the selected Event in the Wwise Sound Engine.
            // gameObject   Refers to the game object in which this script is attached.
            SomeSound.Post(gameObject);
        }
    }
}