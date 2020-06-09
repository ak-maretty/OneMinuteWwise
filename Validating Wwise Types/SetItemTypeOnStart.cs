using System.Collections;
using System.Collections.Generic;
using UnityEngine;
 
public class SetItemTypeOnStart : MonoBehaviour
{
    public AK.Wwise.Switch ItemTypeSwitch;
    //public AK.Wwise.Event SomeEvent;
    //public AK.Wwise.RTPC SomeRTPC;
    //public AK.Wwise.Bank SomeBank;
 
    void Start()
    {
        ItemTypeSwitch.Validate();
        //SomeEvent.Validate();
        //SomeRTPC.Validate();
        //SomeBank.Validate();
 
        if (ItemTypeSwitch.IsValid())
        {
            ItemTypeSwitch.SetValue(gameObject);
        }
        else {
            print("Wwise-Type not assigned on - "+this.gameObject.name);
        }
       
    }
}