
SoloShip Class
==============



Namespace
    :dn:ns:`Clay.Game.Mod.Entities`

Assemblies
    * Clay.Game

----

.. contents::
   :local:



Inheritance Hierarchy
---------------------

* :dn:cls:`System.Object`
* :dn:cls:`Tuna.Mob`
* :dn:cls:`Clay.Game.Mod.Entities.Entity`
* :dn:cls:`Clay.Game.Mod.Entities.Vehicle`
* :dn:cls:`Clay.Game.Mod.Entities.SoloShip`




Syntax
------

.. code-block:: csharp

    public class SoloShip : Vehicle, IComparable, IAudioSourceInfo, ITargettable, IPathFindingAgent





.. dn:class:: Clay.Game.Mod.Entities.SoloShip
    :hidden:

.. dn:class:: Clay.Game.Mod.Entities.SoloShip


Properties
----------

.. dn:class:: Clay.Game.Mod.Entities.SoloShip
    :noindex:
    :hidden:

    .. dn:property:: Clay.Game.Mod.Entities.SoloShip._attributes



        :rtype: Attributes

        .. code-block:: csharp

            public Attributes _attributes { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.SoloShip.firingCharge



        :rtype: System.Single

        .. code-block:: csharp

            public float firingCharge { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.SoloShip.useSpawnEntityCommand



        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool useSpawnEntityCommand { get; }



Methods
-------

.. dn:class:: Clay.Game.Mod.Entities.SoloShip
    :noindex:
    :hidden:

    .. dn:method:: Clay.Game.Mod.Entities.SoloShip.Activate(Attributes, UnityEngine.Vector2, System.Single, Colony, Team)



        :type attr: Attributes

        :type atPosition: UnityEngine.Vector2

        :type atAngle: System.Single

        :type colony: Colony

        :type newTeam: Team


        .. code-block:: csharp

            public override void Activate(Attributes attr, Vector2 atPosition, float atAngle, Colony colony, Team newTeam)

    .. dn:method:: Clay.Game.Mod.Entities.SoloShip.CloneConfiguration(Tuna.Mob)



        :type mob: Tuna.Mob


        .. code-block:: csharp

            public override void CloneConfiguration(Mob mob)

    .. dn:method:: Clay.Game.Mod.Entities.SoloShip.GetCommandLine(System.Boolean)



        :type multiLine: System.Boolean

        :rtype: System.String

        .. code-block:: csharp

            public override string GetCommandLine(bool multiLine)

    .. dn:method:: Clay.Game.Mod.Entities.SoloShip.GetRespawnString()



        :rtype: System.String

        .. code-block:: csharp

            public override string GetRespawnString()

    .. dn:method:: Clay.Game.Mod.Entities.SoloShip.InitialiseApp()




        .. code-block:: csharp

            public static void InitialiseApp()

    .. dn:method:: Clay.Game.Mod.Entities.SoloShip.SpawnSoloShip(System.String[])



        :type parameters: System.String<System.String>[]

        :rtype: Clay.Game.Mod.Entities.SoloShip

        .. code-block:: csharp

            public static SoloShip SpawnSoloShip(string[] parameters)

    .. dn:method:: Clay.Game.Mod.Entities.SoloShip.SpawnSoloShipLua(System.String)



        :type parameters: System.String

        :rtype: Clay.Game.Mod.Entities.SoloShip

        .. code-block:: csharp

            public static SoloShip SpawnSoloShipLua(string parameters)



