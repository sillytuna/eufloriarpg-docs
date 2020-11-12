
Scourge Class
=============



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
* :dn:cls:`Clay.Game.Mod.Entities.Scourge`




Syntax
------

.. code-block:: csharp

    public class Scourge : Vehicle, IComparable, IAudioSourceInfo, ITargettable, IPathFindingAgent





.. dn:class:: Clay.Game.Mod.Entities.Scourge
    :hidden:

.. dn:class:: Clay.Game.Mod.Entities.Scourge


Constructors
------------

.. dn:class:: Clay.Game.Mod.Entities.Scourge
    :noindex:
    :hidden:

    .. dn:constructor:: Clay.Game.Mod.Entities.Scourge.Scourge()




        .. code-block:: csharp

            public Scourge()



Methods
-------

.. dn:class:: Clay.Game.Mod.Entities.Scourge
    :noindex:
    :hidden:

    .. dn:method:: Clay.Game.Mod.Entities.Scourge.Activate(Attributes, UnityEngine.Vector2, System.Single, Colony, Team)



        :type attr: Attributes

        :type atPosition: UnityEngine.Vector2

        :type atAngle: System.Single

        :type colony: Colony

        :type newTeam: Team


        .. code-block:: csharp

            public override void Activate(Attributes attr, Vector2 atPosition, float atAngle, Colony colony, Team newTeam)

    .. dn:method:: Clay.Game.Mod.Entities.Scourge.DamagedBy(Clay.Game.Mod.Entities.Entity, System.Single, Weapon, System.Boolean, System.Boolean)



        :type attacker: Clay.Game.Mod.Entities.Entity

        :type damage: System.Single

        :type weapon: Weapon

        :type effectHandled: System.Boolean

        :type fxHandled: System.Boolean

        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool DamagedBy(Entity attacker, float damage, Weapon weapon, bool effectHandled = false, bool fxHandled = false)

    .. dn:method:: Clay.Game.Mod.Entities.Scourge.Trashed()




        .. code-block:: csharp

            public override void Trashed()

    .. dn:method:: Clay.Game.Mod.Entities.Scourge.Update(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public override void Update(float time)



